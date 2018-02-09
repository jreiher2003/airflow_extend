import logging
from airflow.models import BaseOperator 
from airflow.plugins_manager import AirflowPlugin 
from airflow.utils.decorators import apply_defaults
import requests 

log = logging.getLogger(__name__)

class ZeppelinOperator(BaseOperator): 

	@apply_defaults
	def __init__(self, note_id, *args, **kwargs):
		self.node_id = note_id 
		super(ZeppelinOperator, self).__init__(*args, **kwargs)

	def execute(self, context):
		log.info("Note has begun")
		job = requests.post("http://localhost:8080/api/notebook/job/"+self.node_id)
		if job.status_code == 200:
			log.info("Note has completed successfully: status code"+ str(job.status_code))
		else:
			log.info("ERROR: "+ str(job.status_code))


class ZeppelinPlugin(AirflowPlugin):
	name = "zeppelin_plugin"
	operators = [ZeppelinOperator]



# run zeppelin note from api 

# job = requests.post("http://localhost:8080/api/notebook/job/2D3SJ1XAT")
# if job.status_code == 200:
# 	print "zeppelin note has completed"
# print job
# print dir(job)
# print type(job) 
# print job.status_code
# print job.content
# print job.cookies
# print job.url
# print job.text
# print job.json
# print job.encoding 
# print job.raw 
# print job.next
# print job.ok 


# json_data = json.dump(job.json)
# print json_data
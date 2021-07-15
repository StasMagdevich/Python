import boto3
import hvac
import pymysql
import csv
import os
import pprint
import datetime
query = """
		SELECT query.id,CONCAT(query.name) AS file_name
		FROM query_group JOIN query_container ON container_id = query_container.id 
		JOIN query ON query_group.id = group_id AND query.id in (3851,4276,4535,6928);
		"""
query_unload = """select sql_ from qatestsautomationdb.query where id = {0}"""


def start_job():
		hvac_client = hvac.Client(url='https://vault.infra.slicetest.com/',token='s.jxVZjdijt1u7pjjgngf4bnry')
        #session = boto3.Session()
        #ec2_credentials = session.get_credentials()
        #hvac_client.auth.aws.iam_login(ec2_credentials.access_key, ec2_credentials.secret_key, ec2_credentials.token)

		data = hvac_client.secrets.kv.v2.read_secret_version(path='DATAENGINEERING/PII')
		key_1,password = list(data['data']['data'].items())[0]
		key_2,user = list(data['data']['data'].items())[1]
		# Open database connection
		db = pymysql.connect(host="qamanager-db.slicetest.com", user=user, password=password,database="qatestsautomationdb")
		# prepare a cursor object using cursor() method
		cursor = db.cursor(pymysql.cursors.DictCursor)
		return db, cursor


def git_push():
	now = datetime.datetime.now()
	now = str(now.strftime("%Y-%m-%d %H:%M"))
	os.system("git commit -m '%s'" % now)
	os.system("git push origin master  ")


if __name__=="__main__":
	curr_dir = os.getcwd() + "/"
	pp = pprint.PrettyPrinter(indent=1, width=1000)
	db, cursor = start_job()
	cursor.execute(query)
	rows = cursor.fetchall()
	for row in rows:
		id = row['id']
		file_name = row['file_name']
		file_full_name = curr_dir + file_name + ".sql"
		cursor.execute(query_unload.format(id))
		result = cursor.fetchall()
		if not os.path.exists(os.path.dirname(file_full_name)):
			os.makedirs(os.path.dirname(file_full_name))
		c = csv.writer(open(file_full_name,"w"), quoting=csv.QUOTE_NONE, escapechar='\\')
		s=pp.pformat(result)[11: -3]
		c.writerow([s])
	git_push()
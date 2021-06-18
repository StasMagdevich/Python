import itertools
import pymysql as MySQLdb
import os
import pprint
import datetime

def git_push():
	now = datetime.datetime.now()
	now = str(now.strftime("%Y-%m-%d %H:%M"))
	os.system("git add . ")
	os.system("git commit -m '%s'" % now)
	os.system("git push origin master ")
if __name__=="__main__":
	pp = pprint.PrettyPrinter(indent=1, width=1000)
	db = MySQLdb.connect(host="terminal.dwh.slicetest.com", user="qa", password="1234", database="qatestsautomationdb")
	cursor = db.cursor()
	cursor.execute('select sql_ from qatestsautomationdb.query where id = 3851')
	result = cursor.fetchall()
	myString = ' || '.join(map(str, itertools.chain(*result)))
	cursor.execute('select name from query where id = 3851')
	file_full_name = cursor.fetchall()
	myString2 = ' || '.join(map(str, itertools.chain(*file_full_name)))
	c = open(myString2+'.sql',"w")
	c.write(myString)
	git_push()
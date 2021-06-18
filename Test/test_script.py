import itertools
import pymysql as MySQLdb
import os
import pprint
import datetime


def cleaning():
	os.system("rm -r DQR")


def git_push():
	now = datetime.datetime.now()
	now = str(now.strftime("%Y-%m-%d %H:%M"))
	os.system("git add DQR ")
	os.system("git commit -am '%s'" % now)
	os.system("git push origin master")
if __name__=="__main__":
	cleaning()
	pp = pprint.PrettyPrinter(indent=1, width=1000)
	db = MySQLdb.connect(host="terminal.dwh.slicetest.com", user="qa", password="1234", database="qatestsautomationdb")
	cursor = db.cursor()
	cursor.execute('select sql_ from qatestsautomationdb.query where id in (3851,4276,4535,6928)')
	result = cursor.fetchall()
	myString = '; \n\n '.join(map(str, itertools.chain(*result)))
	#print(myString)
	cursor.execute('select name from query where id in (3851,4276,4535,6928)')
	file_full_name = cursor.fetchall()
	myString2 = ' || '.join(map(str, itertools.chain(*file_full_name)))
	c = open(myString2+'.sql',"w")
	c.write(myString)
	#print(myString2)
	git_push()
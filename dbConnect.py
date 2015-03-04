#!/usr/bin/env python
# -*- coding: utf-8 -*-
__name__ = "dbConnect"
__description__ = 'Light Database Connection Module for Python'
__autor__ = "Emin Mastizada <come@debugwith.me>"
__version__ =  '0.2'

import mysql.connector	# MySQL Connector
from mysql.connector import errorcode
import yaml
settings = yaml.load(open("credentials.yml", 'r'))
### Settings file can be checked for keys:
def check_settings():
	if not 'db' in settings.keys():
		return False
	keys = ['user','password','database']
	return all(key in settings['db'].keys() for key in keys)

def connect():
	"""
	Creates connection to database, returns Connection or boolean False
	"""
	if not check_settings():
		print("Some keys are absent in credentials.yml")
		return False
	try:
		con = mysql.connector.connect(
			user=settings['db']['user'],
			password=settings['db']['password'],
			host=settings['db']['host'],
			database=settings['db']['database'],
			charset='utf8')
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Wrong credentials, ACCESS DENIED")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database %s does not exists" % (settings['db']['database']))
		else:
			print(err) # Change this code, it can be written to log file or just printed.
		return False
	return con

def disconnect(con):
	"""
	Disconnect from db
	"""
	con.close()

"""
Light Database Connection Module for Python
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__name__ = "dbConnect"
__description__ = 'Light Database Connection Module for Python'
__author__ = "Emin Mastizada <come@debugwith.me>"
__version__ = '0.3'
__license__ = "MPL 2.0"
__credits__ = ""

import mysql.connector  # MySQL Connector
from mysql.connector import errorcode
import yaml
from datetime import datetime

credentials_file = open("credentials.yml", 'r')
settings = yaml.load(credentials_file)
credentials_file.close()
connection = None
current = None


def _check_settings():
    """
    Check configuration file
    :return: True if all settings are correct
    """
    if not 'db' in settings.keys():
        return False
    keys = ['user', 'password', 'database']
    return all(key in settings['db'].keys() for key in keys)


def connect():
    """
    Creates connection to database, returns Connection or boolean False
    :return: Mysql Connection
    """
    if not _check_settings():
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
            print(err)  # Change this code, it can be logged or just printed.
        return False
    connection = con
    current = con.cursor()
    return con, current


def disconnect(con):
    """
    Disconnect from database
    :param con: Database connection to be closed
    """
    con.close()


def insert_dict(data, table, con=connection, cur=current):
    """
    Insert dictionary object to database
    :type data: dict
    :param data: Object with keys as column name in database
    :type table: str
    :param table: Table name
    :param con: Connection, no need
    :param cur: Current, no need
    :return: dict with Boolean status key and message
    """
    if not con:
        return {'status': False, 'message': "Connection is not defined"}
    if not cur:
        return {'status': False, 'message': "Current is not defined"}
    if not len(data):
        return {'status': False, 'message': "Object is empty"}
    # Make datetime and date objects string:
    try:
        for key in data:
            if isinstance(data[key], datetime):
                data[key] = str(data[key].isoformat())
        # Build query:
        query = "INSERT INTO %s (" % table
        query_v = "VALUES ("
        for key in data:
            query += key + ','
            if isinstance(data[key], str):
                query_v += "'{" + key + "}',"
            else:
                query_v += "{" + key + "},"
        query = query.rstrip(",")
        query_v = query_v.rstrip(",")
        query = query + ") " + query_v + ") "
        # Format, execute and send to database:
        cur.execute(query.format(**data))
        con.commit()
    except Exception as e:
        return {'status': False, 'message': e}
    return {'status': True, 'message': "Object added to database"}

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
MySQL for Humans
"""
__name__ = "dbConnect"
__description__ = 'MySQL for Humans'
__author__ = "Emin Mastizada <emin@linux.com>"
__version__ = '1.0'
__license__ = "MPL 2.0"

import mysql.connector  # MySQL Connector
from mysql.connector import errorcode
import json


class DBConnect():
    """
    Light database connection object
    """
    @staticmethod
    def _check_settings(self):
        """
        Check configuration file
        :return: True if all settings are correct
        """
        keys = ['host', 'user', 'password', 'database']
        if not all(key in self.settings.keys() for key in keys):
            raise ValueError('Please check credentials file for correct keys: host, user, password, database')

    def connect(self):
        """
        Creates connection to database, sets connection and cursor
        Connection to database can be loosed, if that happens you can use this function to reconnect to database
        """
        try:
            self.connection = mysql.connector.connect(
                user=self.settings['user'],
                password=self.settings['password'],
                host=self.settings['host'],
                database=self.settings['database'],
                charset='utf8')
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Wrong credentials, ACCESS DENIED")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database %s does not exists" % (self.settings['database']))
            else:
                raise ValueError(err)
        self.cursor = self.connection.cursor()

    def __init__(self, credentials_file='credentials.json', host=None, user=None, password=None, database=None):
        """
        Initialise object with credentials file provided
        """
        if host and user and password and database:
            self.settings = {"host": host, "user": user, "password": password, "database": database}
        else:
            self.settings = json.load(open(credentials_file, 'r'))
        self._check_settings(self)
        self.connection = None
        self.cursor = None
        self.connect()

    def disconnect(self):
        """
        Disconnect from database
        """
        self.connection.close()

    def fetch(self, table, limit=1000, fields=None, filters=None, case='AND'):
        """
        Get data from table
        :param table: name of the table
        :param limit: result limit for fetch
        :param fields: fields to get
        :param filters: filters to get custom results (where)
        :param case: [AND, OR] for filter type
        :return: array of dictionary with column name and value
        """
        if fields:
            query = 'SELECT '
            for field in fields:
                query += field + ', '
            query = query.rstrip(', ') + ' FROM ' + str(table)
        else:
            query = 'SELECT * FROM %s' % table
        if filters:
            query += ' WHERE '
            for key in filters:
                query += key + ' = ' + '%(' + key + ')s ' + case + ' '
            query = query.rstrip(case + ' ')
        query += ' LIMIT ' + str(limit)
        if filters:
            self.cursor.execute(query, filters)
        else:
            self.cursor.execute(query)
        items = self.cursor.fetchall()
        if fields:
            columns = fields
        else:
            columns = [i[0] for i in self.cursor.description]
        results = []
        for item in items:
            data = {}
            for i in range(len(columns)):
                data[columns[i]] = item[i]
            results.append(data)
        return results

    def insert(self, data, table, commit=True, update=None):
        """
        Insert dictionary object to database
        :type data: dict
        :param data: Object with keys as column name in database
        :type table: str
        :param table: Table name
        :param commit: Commit after every insert
        :type update: dict
        :param update: Update selected columns if key is duplicate
        :return: dict with Boolean status key and message
        """
        if not self.connection:
            return {'status': False, 'message': "Connection is not defined"}
        if not self.cursor:
            return {'status': False, 'message': "Cursor is not defined"}
        if not len(data):
            return {'status': False, 'message': "Object is empty"}
        # Make datetime and date objects string:
        try:
            query_insert = "INSERT INTO %s (" % table
            query_value = " VALUES ("
            for key in data:
                query_insert += key + ', '
                query_value += '%(' + key + ')s, '
            query_insert = query_insert.rstrip(', ') + ')'
            query_value = query_value.rstrip(', ') + ')'
            query = query_insert + query_value
            if update and len(update.keys()):
                query += ' ON DUPLICATE KEY UPDATE '
                for key in update:
                    query += key + ' = '
                    if isinstance(update[key], int):
                        query += update[key] + ', '
                    else:
                        query += '"' + update[key] + '", '
                query = query.rstrip(', ')
            # Format, execute and send to database:
            self.cursor.execute(query, data)
            if commit:
                self.connection.commit()
        except Exception as e:
            if not isinstance(e, str):
                e = str(e)
            return {'status': False, 'message': e}
        return {'status': True, 'message': "Object added to database"}

    def update(self, data, filters, table, case='AND', commit=True):
        """
        Update database using information in dictionary
        :type data: dict
        :param data: Object with keys as column name in database
        :type filters: dict
        :param filters: Objects with keys as column name for filters statement
        :type table: str
        :param table: Table name
        :return: dict with Boolean status key and message
        """
        if not self.connection:
            return {'status': False, 'message': "Connection is not defined"}
        if not self.cursor:
            return {'status': False, 'message': "Cursor is not defined"}
        if not len(data):
            return {'status': False, 'message': "Object is empty"}
        # Make datetime and date objects string:
        try:
            # Build query:
            query_update = "UPDATE %s SET " % table
            for key in data:
                query_update += key + ' = %(' + key + ')s, '
            query_update = query_update.rstrip(', ') + ' '  # remove last comma and add empty space
            query_update += 'WHERE '
            for key in filters:
                query_update += key + ' = %(where_' + key + ')s ' + case + ' '
            query_update = query_update.rstrip(case + ' ')
            # merge filters and data:
            for key in filters:
                data['where_' + key] = filters[key]
            # execute and send to database:
            self.cursor.execute(query_update, data)
            if commit:
                self.connection.commit()
        except Exception as e:
            if not isinstance(e, str):
                e = str(e)
            return {'status': False, 'message': e}
        return {'status': True, 'message': "Object added to database"}

    def delete(self, table, filters=None, case='AND', commit=True):
        """
        Delete item from table
        :param table: name of table
        :param filters: filter for item(s) to be deleted
        :param case: [AND, OR] case for filter
        """
        if not filters:
            raise ValueError("You must provide filter to delete some record(s). For all records try truncate")
        query = "DELETE FROM %s WHERE " % table
        for key in filters:
            query += key + ' = %(' + key + ')s ' + case + ' '
        query = query.rstrip(case + ' ')
        self.cursor.execute(query, filters)
        if commit:
            self.connection.commit()

    def commit(self):
        """
        Commit collected data for making changes to database
        """
        self.connection.commit()

if __name__ == '__main__':
    pass

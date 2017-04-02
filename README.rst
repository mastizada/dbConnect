dbConnect: Database for Humans
===========================
.. image:: https://readthedocs.org/projects/dbconnect/badge/?version=latest
  :target: http://dbconnect.readthedocs.org/?badge=latest
  :alt: Documentation Status
.. image:: https://travis-ci.org/mastizada/dbConnect.svg?branch=master
  :target: https://travis-ci.org/mastizada/dbConnect
.. image:: https://landscape.io/github/mastizada/dbConnect/master/landscape.svg?style=flat
   :target: https://landscape.io/github/mastizada/dbConnect/master
   :alt: Code Health


WHY?
====

dbConnect was made as a little module to be used in small projects
that need to do some interactions with MySQL or PostgreSQL databases.

It's just a big time saver for developers specially for making data analyzing and data scraping
and it helps to keep your code clean and readable by using python-like structure.


Installation
=============
requirements:
^^^^^^^^^^^^^
dbConnect uses mysql.connector module for mysql, install it using:

.. code-block:: bash

  $ apt-get install python3-mysql.connector
  $ apt-get install python-mysql.connector

Or using offical site: `https://dev.mysql.com/downloads/connector/python/`

For PostgreSQL install psycopg2 module:

.. code-block:: bash

  $ pip install psycopg2

using pip:
^^^^^^^^^^

.. code-block:: bash

	$ pip install dbConnect

from source code:
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ git clone git@github.com:mastizada/dbConnect.git
	$ cd dbConnect
	$ # install required module for database
	$ sudo python setup.py install

Usage
=====
Importing and making a connection:

.. code-block:: python

	>>> from dbConnect import DBConnect
	>>> database = DBConnect(credentials.json)
	>>> database.fetch('tableName', limit=5, filters={'company': 'pyninjas'})

Documentation
=============

- Docs: http://dbconnect.readthedocs.org/
- Alternate Docs: https://pythonhosted.org/dbConnect/
- Check generated documentation using:

	.. code-block:: bash

		$ pydoc3 dbConnect

	or

	.. code-block:: bash

		$ pydoc3 -p 8000

	and open http://localhost:8000/ in browser

Enjoy
=====

dbConnect: MySQL for Humans
===========================
.. image:: https://readthedocs.org/projects/dbconnect/badge/?version=latest
  :target: http://dbconnect.readthedocs.org/?badge=latest
  :alt: Documentation Status
.. image:: https://travis-ci.org/mastizada/dbConnect.svg?branch=master
  :target: https://travis-ci.org/mastizada/dbConnect

Installation
=============
requirements:
^^^^^^^^^^^^^
dbConnect uses mysql.connector module, install it using:

.. code-block:: bash

  $ apt-get install python3-mysql.connector
  $ apt-get install python-mysql.connector

Or using offical site: `https://dev.mysql.com/downloads/connector/python/`

using pip:
^^^^^^^^^^

.. code-block:: bash

	$ pip install dbConnect

from source code:
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

	$ git clone git@github.com:mastizada/dbConnect.git
	$ cd dbConnect
	$ sudo pip install -r requirements.txt --allow-external mysql-connector-python
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
- Another Docs: https://pythonhosted.org/dbConnect/
- Check generated documentation using:

	.. code-block:: bash

		$ pydoc3 dbConnect

	or

	.. code-block:: bash

		$ pydoc3 -p 1994

	and open localhost:1994/ in browser

Enjoy
=====

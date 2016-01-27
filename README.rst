dbConnect: MySQL for Humans
===========================

.. image:: https://readthedocs.org/projects/dbconnect/badge/?version=latest)](https://readthedocs.org/projects/dbconnect/?badge=latest

Installation
=============
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

.. raw:: html
	
	<a href="http://mastizada.com">
		<img src="https://ga-beacon.appspot.com/UA-36541010-2/dbConnect/Readme" />
	</a>
.. _quickstart:

Quickstart
==========

.. module:: dbConnect
.. class:: DBConnect

This page gives a good introduction in how to get started
with dbConnect.

First, make sure that:

* dbConnect is :ref:`installed <install>`

Lets go over every function.


Connection
----------

dbConnect uses ``credentials.json`` file from your project directory by default.
You can give custom path for that file:

	>>> database = DBConnect('/home/user/project/credentials.json')

Or provide database details:

	>>> database = DBConnect(host='127.0.0.1', user='root', password='', database='test')

After successfull connection there will be **database.connection** and
**database.cursor** variables that can be used as in official MySQL
documentation.


Fetch Data
----------

Get data from table.

Basic usage:

	>>> database.fetch('table_name')

Fields:
	- table: ``str`` : name of table, must be provided
	- limit: ``int`` : result limit, default ``1000``
	- fields: ``array`` : list of column names, default ``None``
	- filters: ``dict`` : dictionary with keys as column name, default ``None``
	- case: ``str`` : search case for filter [AND, OR], default ``'AND'``

Example:

	>>> database.fetch('user', limit=5, fields=['id', 'name', 'email'], filters={'company': 'pyninjas'})


Insert Data
-----------

Add new row (data) to table.

Fields:
	- data: ``dict`` : dictionary with keys as column name, must be provided
	- table: ``str`` : name of table, must be provided
	- commit: ``bool`` : commit after insert command, default: True

Example:

	>>> new_user = {'name': 'Emin', 'company': 'pyninjas', 'website': 'mastizada.com'}
	>>> database.insert(new_user, 'user')  # Adds new_user to user table


Update Data
-----------

Update existing row.

Fields:
	- data: ``dict`` : dictionary with keys as column name that will be changed, must be provided
	- filters: ``dict`` : filters to find row(s) that will be changed, must be provided
	- table: ``str`` : name of table, must be provided
	- case: ``str`` : search case for filter [AND, OR], default ``'AND'``

Example:

	>>> database.update({'name': 'Emin Mastizada'}, {'id': 1, 'name': 'Emin'}, 'user', case='OR')


Delete Data
-----------

Delete row from database.

Fields:
	- table: ``str`` : name of table, must be provided
	- filters: ``dict`` : filters to find row(s) that will be deleted, must be provided
	- case: ``str`` : search case for filter [AND, OR], default ``'AND'``

Example:

	>>> database.delete('user', {'id': 1, 'name': 'Emin Mastizada'}, case='OR')


Commit Data
-----------

Commit changes to database.

No fields.

Example:

	>>> database.commit()


And now enjoy and give me your feedbacks ;)

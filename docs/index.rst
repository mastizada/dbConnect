.. dbConnect documentation master file, created by
   sphinx-quickstart on Wed Sep  2 07:30:57 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dbConnect: Database for Humans
======================================

Release v\ |version|. (:ref:`Installation <install>`)

.. image:: https://readthedocs.org/projects/dbconnect/badge/?version=latest

dbConnect is an :ref:`MPLv2 Licensed<mpl2>` Module for **little projects**
using *mysql* or *postgresql* databases. It generates mysql and postgresql
queries automatically, you just send data in pythonic style and it does the rest.

    >>> from dbConnect import DBConnect
    >>> database = DBConnect('credentials.json')
    >>> users = database.fetch('users', limit=5, filters={'status': 'active'})
    >>> new_user = {'name': 'Emin', 'status': 'active', 'company': 'pyninjas'}
    >>> database.insert(new_user, 'users')


Feature Support
---------------
- **fetch** all fields in table as dictionary (column name: value)
- fetch only selected fields
- fetch using filters
- limit fetch result
- filter case [AND, OR]
- **insert** to table
- **update** row
- **delete** row
- **increment** column in table
- **sum** of a numeric column(s)
- **custom sql query**


User Guide
----------

.. toctree::
   :maxdepth: 2

   user/intro
   user/install
   user/quickstart

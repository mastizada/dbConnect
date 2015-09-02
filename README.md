#dbConnect
===
Light MySQL Database operations module

## INSTALL:
* ``pip install dbConnect``

## INSTALLING FROM SOURCE:
* Clone from repository:
  - ``git clone git@github.com:EmiXLabs/dbConnect.git``
* Go to dbConnect folder
  - ``cd dbConnect``
* Install requirements:
  - ```sudo pip install -r requirements.txt --allow-external mysql-connector-python```
* Install package:
  - ``sudo python setup.py install``

##USAGE:
* Import and make connection:
    - ``from dbConnect import DBConnect``
    - ``database = DBConnect(credentials.json file)``
    - ``database.fetch('tableName', limit=5, filters={'company': 'pyninjas'})``

## DOCUMENTATION:
* Read the docs will be here
* Check generated documentation using ``pydoc3 dbConnect`` or ``pydoc3 -p 1994`` and open localhost:1994/ in browser

### Enjoy

[![Analytics](https://ga-beacon.appspot.com/UA-36541010-2/dbConnect/Readme)](http://www.mastizada.com)

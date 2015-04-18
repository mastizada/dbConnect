MySQL Database Connection Module: dbConnect
-------------

**INSTALL**:

* Clone repository to your project folder:

    ``git submodule add https://github.com/EmiXLabs/dbConnect.git``
* Go to dbConnect folder

    ``cd dbConnect``
* Install requirements:
  - Python 3
    ```
    sudo pip3 install -r requirements.txt --allow-external mysql-connector-python
    ```
  - Python 2:
    ```
    sudo pip install -r requirements.txt --allow-external mysql-connector-python
    ```
* Create credentials.yml in your project, example of file is in dbConnect folder.

**USAGE Example**:
```
from dbConnect import dbConnect
# Make connection:
con, cur = dbConnect.connect()

# Some code
cur.execute("select * from listings order by id desc limit 5")

dbConnect.disconnect(con)
```

**DOCUMENTATION**:

* Currently there is no documentation (coming soon staff)
* Check generated documentation using ``pydoc3 dbConnect`` or ``pydoc3 -p 1994`` and open localhost:1994/ in browser

[![Analytics](https://ga-beacon.appspot.com/UA-36541010-2/dbConnect/Readme)](http://www.mastizada.com)

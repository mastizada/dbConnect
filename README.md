MySQL Database Connection Module: dbConnect
-------------

**INSTALL**:

* Clone repository to your project folder.
* Go to dbConnect folder
* Install requirements:
- Python 3
```
sudo pip3 install -r requirements.txt --allow-external mysql-connector-python
```
- Python 2:
```
sudo pip install -r requirements.txt --allow-external mysql-connector-python
```

**USAGE**:
```
from dbConnect import dbConnect
# Make connection:
con = dbConnect.connect()
# Make cursor on connection:
cur = con.cursor()

# Some code
cur.execute("select * from listings order by id desc limit 5")

dbConnect.disconnect(con)
```

[![Analytics](https://ga-beacon.appspot.com/UA-36541010-2/dbConnect/Readme)](http://www.mastizada.com)

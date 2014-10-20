MySQL Database Connection Module: dbConnect
-------------

**INSTALL**:
- Python 3
```
sudo pip3 install -r requirements.txt --allow-external mysql-connector-python
```
- Python 2:
```
sudo pip install -r requirements.txt --allow-external mysql-connector-python
```
Copy Files (credentials.yml, dbConnect.py) to Project Folder

**USAGE**:
```
import dbConnect
con = dbConnect.connect()
cur = con.cursor()

# Some code

dbConnect.disconnect(con)
```

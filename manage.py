from pymongo import MongoClient
import sqlite3

conn = sqlite3.connect('Cybernation.db')

client = MongoClient ('localhost', 27017)
db = client.Cybernation

def savedevice(data):
    collection = db.devices
    collection.insert_one(data)
    
def getAlldevice(user):
    collection = db.devices
    x = collection.find({"userID" : user["_id"]})
    return x

def getdevice(IP):
    collection = db.devices
    x = collection.find_one({"IP":IP})
    return x

def deleteDevice(IP):
    collection = db.devices
    collection.delete_one({"IP":IP})

def saveUser(fname,lname,gen,org,uname,passw):
    # collection = db.User
    # data = {
    #     "Fname": fname,
    #     "Lname": lname,
    #     "Gender":gen,
    #     "Org": org,
    #     "Username" : uname,
    #     "Password" : passw,
    # }
    # collection.insert_one(data)

    chk = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Users';")
    print(chk)
    if not chk :
        conn.execute('''
        CREATE TABLE Users(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Fname           TEXT     NOT NULL,
            Lname           TEXT     NOT NULL,
            Gender          TEXT     NOT NULL,
            Org             TEXT     NOT NULL,
            Username        TEXT     NOT NULL,
            Password        TEXT     NOT NULL);''')
        
    conn.execute(f'''INSERT INTO Users VALUES ({fname},{lname},{gen},{org},{uname},{passw})''')





# conn.execute('''
# CREATE TABLE Devices(
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# UserID         INTEGER  NOT NULL,
# Name           TEXT     NOT NULL,    
# IP             TEXT     NOT NULL,
# Subnet         TEXT     NOT NULL,
# Description    TEXT     NOT NULL,
# Type           TEXT     NOT NULL,
# Username       TEXT     NOT NULL,
# Password       TEXT     NOT NULL,
# Enable         TEXT     NOT NULL,
# Last_Modify    DATETIME NOT NULL);''')

# conn.execute('''
# CREATE TABLE CONFIGS(
# ID INTEGER PRIMARY KEY AUTOINCREMENT,
# deviceID       INTEGER  NOT NULL,
# Name           TEXT     NOT NULL,

# Last_Modify    DATETIME NOT NULL,);''')
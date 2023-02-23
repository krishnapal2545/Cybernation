from pymongo import MongoClient

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
    collection = db.User
    data = {
        "Fname": fname,
        "Lname": lname,
        "Gender":gen,
        "Org": org,
        "Username" : uname,
        "Password" : passw,
    }
    collection.insert_one(data)


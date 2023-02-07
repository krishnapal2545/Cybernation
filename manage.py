from pymongo import MongoClient

client = MongoClient ('localhost', 27017)
db = client.Cybernation



def savedevice(name,ip, desc, dtype, ssh_u, ssh_p, LM):
    collection = db.devices
    data = {
        "Name": name,
        "IP": ip,
        "Description": desc,
        "Type" : dtype,
        "Username" : ssh_u,
        "Password" : ssh_p,
        "Last_Modify" : LM,
        "Config" : {}
    }
    collection.insert_one(data)

def getAlldevice():
    collection = db.devices
    x = collection.find()
    return x

def getdevice(IP):
    collection = db.devices
    x = collection.find_one({"IP":IP})
    return x
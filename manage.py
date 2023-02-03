from pymongo import MongoClient

client = MongoClient ('localhost', 27017)
db = client.Cybernation



def savedevice(name,ip, desc, type, ssh_u, ssh_p):
    collection = db.devices
    data = {
        "Name": name,
        "IP": ip,
        "Description": desc,
        "Type" : type,
        "Username" : ssh_u,
        "Password" : ssh_p,
        "Config" : {}
    }
    collection.insert_one(data)
    
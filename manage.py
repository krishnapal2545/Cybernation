from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.database

collection = db.devices

device_1 = {
    "name": "Krishna",
    "IP": "193.192.180.08",
    "Description": "Time Pass"
}

add = collection.insert_one(device_1)
print(add)

cursor = collection.find()
for record in cursor:
    print(record)
import pymongo
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.6wagv.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

dic = {"name": "abhishek",
       "value" : "abhi@gmail.com",
       "surname": "emmanual"}


dic2 = {"name": "abhishek",
       "value" : "abhi@gmail.com",
       "surname": "emmanual"}
dic3 = {"name": "abhishek",
       "value" : "abhi@gmail.com",
       "surname": "emmanual"}
print(dic)

db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(dic)




















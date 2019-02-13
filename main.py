import pymongo
from pymongo import MongoClient

myClient = MongoClient()
db = myClient.mydb
Users = db.users

users = [{"username": "nick", 
         "password": "mypassword",
         "favorite_number": 445,
         "hobbies": ["python", "games","chocolate"]}, 
        {"username": "secondone", 
         "password": "Yes!145",
         "favorite_number": 445}]

inserted = Users.insert_many(users)
print(inserted.inserted_ids)

#To see what is in my db
Users.find().count()
Users.find({"username": "nick"}).count()
Users.find({"username": "nick","password": "mypassword"}).count()
#where not
Users.find({"username": {"$ne": "nick"}}).count()

db.users.create_index([("username", pymongo.ASCENDING)])


#Date time
import datetime
current_date = datetime.datetime.now()
old_date = datetime.datetime(2009, 8, 11)
uld = Users.insert_one({"username": "Fie", "date": current_date})

#For documents where date is greater or equal to old_date
Users.find({"date": {"$gte": old_date}}).count()
Users.find({"date": {"$lte": old_date}}).count()
Users.find({"date": {"$exists": True}}).count()
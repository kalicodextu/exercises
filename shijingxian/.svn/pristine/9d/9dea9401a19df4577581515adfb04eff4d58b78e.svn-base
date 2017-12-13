import pymongo
from pymongo import MongoClient
import datetime
import pprint
from bson.objectid import ObjectId

client = MongoClient('localhost',27017)

post ={
    "author":"Mike",
    "text":"My first blog post!",
    "tags":["mongodb","python","pymongo"],
    "date":datetime.datetime.utcnow()
    }


db = client.test_database

#collection = db.test_collection

posts = db.posts
post_id=posts.insert_one(post).inserted_id
print(post_id)

#print(db.test_collection)
pprint.pprint(posts.find_one({"_id":post_id}))
#clear the database
result = db.posts.delete_many({"_id":post_id})
print(result.deleted_count)

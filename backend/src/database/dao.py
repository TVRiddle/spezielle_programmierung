import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb")
# cluster = MongoClient("mongodb://localhost:4444/?compressors=disabled&gssapiServiceName=mongodb")
db = cluster["test"]
collection = db["test"]

bit = {"name": "test"}

collection.insert_one(bit)
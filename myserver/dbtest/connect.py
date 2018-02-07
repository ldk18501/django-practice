from pymongo import MongoClient
import os


class MongoConnection():
    def __init__(self, dbName):
        client = MongoClient(os.environ['MONGO_URL'], 27017)
        self.db = client[dbName]

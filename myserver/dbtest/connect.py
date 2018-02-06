from pymongo import MongoClient


class MongoConnection():
    def __init__(self, dbName):
        client = MongoClient('localhost', 27017)
        self.db = client[dbName]

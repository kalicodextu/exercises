from pymongo import MongoClient


class MongoBase(object):
    def __init__(self):
        self.client =  MongoClient('mongodb://localhost:27017/')
         
    def conCollection(self, collection_name):
        try:
            self.collection = self.client[collection_name]
            return self.collection
        except:
            return False
        else:
            return True

    def getDocument(self, query_object):
        try:
            self.document = self.collection.find_one(query_object)
            return self.document
        except:
            return False
        else:
            return True

    def getData(self, query_object, query_key):
        try:
            self.getDocument(query_object)
            self.data = self.document
            return self.data
        except:
            return False
        else:
            return True

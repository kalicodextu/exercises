from pymongo import MongoClient


class MongoBase(object):
    def __init__(self):
        self.client =  MongoClient('mongodb://localhost:27017/')
        self.db = self.client['TestDB']
         
    def conCollection(self, collection_name):
        try:
            self.collection = self.db[collection_name]
        except Exception as e:
            raise 'conCollection: ' + str(e)
            

    def getDocument(self, query_object):
        try:
            self.document = self.collection.find_one(query_object)
        except Exception as e:
            raise 'getDocument: ' + str(e)

    def getData(self, query_key):
        try:
            self.data = self.document[query_key]
        except Exception as e:
            raise 'getData: ' + str(e)
        

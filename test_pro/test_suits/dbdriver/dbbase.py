from pymongo import MongoClient


class MongoBase(object):
    def __init__(self):
        self.client =  MongoClient('mongodb://localhost:27017/')

    def switchDatabase(self, db_name):
        self.database = self.client[db_name]

    def conCollection(self, collection_name):
        try:
            self.collection = self.database[collection_name]
        except Exception as e:
            print 'conCollection: ' + str(e)
            raise e

    def getDocument(self, query_object):
        try:
            self.document = self.collection.find_one(query_object)
        except Exception as e:
            print 'getDocument: ' + str(e)
            raise e

    def delDocument(self, query_object):
        try:
            self.collection.remove(query_object)
        except Exception as e:
            print 'delDocument: ' + str(e)
            raise e
    
    def delField(self, query_object, query_key):
        try:
            self.data = self.collection.find_one_and_update(query_object,
                    {'$unset': {query_key: ''}})
        except Exception as e:
            print 'delField: ' + str(e)
            raise e

    def getData(self, query_key):
        try:
            self.data = self.document[query_key]
        except Exception as e:
            print 'getData: ' + str(e)
            raise e
    

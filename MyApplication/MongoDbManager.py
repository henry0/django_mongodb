import pymongo
from bson.objectid import ObjectId


class MongoDbManager:
    _instance = None
    conn = pymongo.MongoClient(host='localhost',
                               port=27017)
    _database = conn['MyApplicationDB']['MyApplicationCollection']

    database = conn['MyApplication']
    collection = database['MyApplicationCollection']

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

    def set_database(self, database, collection):
        self.database = self._instance.conn[database]
        if collection is not None:
            self.collection = self.database[collection]
        return self._instance

    def set_collection(self, collection):
        assert self.database
        self.collection = self.database[collection]
        return self._instance

    def insert_document(self, document):
        assert self.database
        self.collection = self.database['Documents']
        if type(document) is list:
            return self.collection.insert_many(document)
        else:
            return self.collection.insert_one(document)

    def update_document(self, _id, document):
        assert self.database
        self.collection = self.database['Documents']
        one = self.get_document(_id)
        sets = {}
        unset = {}
        for key in document:
            if one[key] is None:
                unset.update({key: document[key]})
            else:
                sets.update({key: document[key]})

        print('sets')
        print(sets)

        for key in one:
            if key == '_id':
                pass
            else:
                if type(one[key]) is list:
                    unset.update({key: ''})
                try:
                    if document[key] is None:
                        pass
                except KeyError:
                    unset.update({key: ''})

        print('unset')
        print(unset)

        self.collection.update_one(
            {"_id": ObjectId(_id)},
            {
                "$unset": unset
            }
        )

        self.collection.update_one(
            {"_id": ObjectId(_id)},
            {
                "$set": sets
            }
        )

        return self._instance

    def get_document(self, _id):
        assert self._database
        return self.collection.find_one(_id)

    '''
    def get_users_from_collection(self, _query):
        assert self._database
        return self._database.find(_query)

    def add_user_on_collection(self, _data):
        if type(_data) is list:
            return self._database.insert_many(_data)
        else:
            return self._database.insert_one(_data)
    '''

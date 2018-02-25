import os
import sys

from pymongo import MongoClient

import config


class Database:
    DATABASE = config.DATABASE
    LINK = config.MONGO_LINK.format(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    def __init__(self, collection):
        from pymongo.errors import ConnectionFailure
        try:
            self.db = MongoClient(self.LINK)[self.DATABASE][collection]
            print('Connect to {} successful'.format(collection))
        except ConnectionFailure:
            print('Connecting to {} error'.format(collection))
            sys.exit()

    def add_doc(self, doc):
        if self.db.find_one({'_id': doc['_id']}) is None:
            self.db.save(doc)
            return True
        return False

    def change_doc(self, _id, mode):
        self.db.find_one_and_update(_id, {'$set': mode})

    def delete_doc(self, _id):
        self.db.find_one_and_delete(_id)

    def get_docs(self, query=None):
        if query is None:
            query = {}
        return self.db.find(query)

    def get_one_doc(self, _id):
        return self.db.find_one(_id)

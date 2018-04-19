import pymongo
from pymongo import MongoClient
import datetime
import json
client = MongoClient()



if __name__ == '__main__':

    list = {
        'positionId' : 456789,
        'postionName' : 'Police',
        'Company' : 'America'
    }

    data = json.dumps(list,indent=4)
    print data
    client = MongoClient()
    db = client.test_database
    coll = db.test_collection
    result = db.coll.insert_one(list)

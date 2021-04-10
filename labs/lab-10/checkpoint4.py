from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId
client = MongoClient()

if __name__ == '__main__':
    pp = pprint.PrettyPrinter(indent=4)

    db = client.mongo_db_lab
    collection = db.definitions

    # Fetch all records
    print("Fetching all records....")
    pp.pprint(list(collection.find()))

    # Fetch one record
    print("Fetch one record...")
    pp.pprint(collection.find_one())

    # Fetch a specific record by Object ID
    print("Fetching a specific record...")
    pp.pprint(collection.find_one({"_id" : ObjectId("56fe9e22bad6b23cde07b8b8")}))

    # Insert a object
    print("Inserting an object...")
    collection.insert_one({"word" : "yogurt", "definition" : "worlds best snack"})
    pp.pprint(collection.find_one({"word" : "yogurt"}))

from pymongo import MongoClient
import pprint
import datetime
import random
client = MongoClient()


def random_word_requester():
    db = client.mongo_db_lab
    collection = db.definitions

    randIndex = random.randint(0, collection.count())
    randomWord = list(collection.find())[randIndex]
    collection.update_one({"word" : randomWord["word"]}, {"$push" : {"dates" : datetime.datetime.utcnow().isoformat()}})
    return randomWord


if __name__ == '__main__':
    print(random_word_requester())


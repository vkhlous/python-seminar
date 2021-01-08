from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import quote

class DistanceRepository(object):

    def __init__(self):
        # initializing the MongoClient, this helps to
        self.client = MongoClient(
            "mongodb://VKhlous:"+quote("Lg@YUMlowp")+"@13.48.133.235:27017/?authSource=conTraDB&readPreference=primary&appname=MongoDB%20Compass&ssl=false")
        self.database = self.client['conTraDB']

    def create(self, distance):
        if distance is not None:
            print("Distance saved\n")
            self.database.Distances.insert(distance.get_as_json())
        else:
            raise Exception("Nothing to save, because project parameter is None")

    def read(self, id=None):
        if id is None:
            return self.database.Distances.find({})
        else:
            return self.database.Distances.find({"_id":id})

    def update(self, distance):
        if distance is not None:
            # the save() method updates the document if this has an _id property
            # which appears in the collection, otherwise it saves the data
            # as a new document in the collection
            self.database.Distances.save(distance.get_as_json())
        else:
            raise Exception("Nothing to update, because project parameter is None")

    def delete(self, distance):
        if distance is not None:
            self.database.Distances.remove(distance.get_as_json())
        else:
            raise Exception("Nothing to delete, because project parameter is None")
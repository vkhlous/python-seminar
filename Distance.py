from bson.objectid import ObjectId
import datetime

class Distance(object):

    def __init__(self,
                 location_id=None,
                 tag1_id=0,
                 tag2_id=0,
                 distance=0,
                 counter=0):
        if location_id is None:
            self._id = ObjectId()
        else:
            self._id = location_id

        self.tag1_id = tag1_id
        self.tag2_id = tag2_id
        self.distance = distance
        self.time = datetime.datetime.now()
        self.test_name = "{Name of the location}"
        self.counter = counter
    def get_as_json(self):
        return self.__dict__

    @staticmethod
    def build_from_json(json_data):
        """ Method used to build Project objects from JSON data returned from MongoDB """
        if json_data is not None:
            try:
                return Distance(json_data.get('_id', None),
                                   json_data.get('tag1_id'),
                                   json_data.get('tag2_id'),
                                   json_data.get('distance'),
                                   json_data.get('time'),
                                   json_data.get('name'),
                                   json_data.get('counter'))
            except KeyError as e:
                raise Exception("Key not found in json_data: {}".format(e.message))
        else:
            raise Exception("No data to create TagLocation from!")

    @property
    def id(self):
        return self._id

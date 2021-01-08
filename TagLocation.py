from bson.objectid import ObjectId
import datetime

class TagLocation(object):

    def __init__(self,
                 location_id=None,
                 tag_id=None,
                 x_coordinate=0.0,
                 y_coordinate=0.0,
                 z_coordinate=0.0,
                 quality_factor=0,
                 correlation_nr=0):
        if location_id is None:
            self._id = ObjectId()
        else:
            self._id = location_id

        self.tag_id = tag_id
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.z_coordinate = z_coordinate
        self.quality_factor = quality_factor
        self.correlation_nr = correlation_nr
        self.time = datetime.datetime.now()
        self.name = "{Name of the location}"
    def get_as_json(self):
        return self.__dict__

    @staticmethod
    def build_from_json(json_data):
        """ Method used to build Project objects from JSON data returned from MongoDB """
        if json_data is not None:
            try:
                return TagLocation(json_data.get('_id', None),
                                   json_data.get('tag_id'),
                                   json_data.get('x'),
                                   json_data.get('y'),
                                   json_data.get('z'),
                                   json_data.get('quality'),
                                   json_data.get('correlation_nr'),
                                   json_data.get('time'),
                                   json_data.get('name'))
            except KeyError as e:
                raise Exception("Key not found in json_data: {}".format(e.message))
        else:
            raise Exception("No data to create TagLocation from!")

    @property
    def id(self):
        return self._id


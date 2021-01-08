from bson.objectid import ObjectId
from TagLocation import TagLocation
from TagLocationRepository import TagLocationRepository

from Distance import Distance
from DistanceRepository import DistanceRepository
from bson.objectid import ObjectId
import json
import re
import base64


class TagLocationService(object):

    @staticmethod
    def process_message(message, counter):
        print("Processing message...")
        # 1) Get tag Id (will omit it for now)
        msg_text = str(message.payload.decode("utf-8"))
        topic = message.topic.split('/')
        tag_id = topic[2]
        try:

            if message:
                if topic[4] == 'location':
                    # 2) Decode and add to DB
                    json_msg = json.loads(msg_text)
                    tag_location = TagLocation(json_msg.get('position').get('_id', None),
                                               tag_id,
                                               json_msg.get('position').get('x'),
                                               json_msg.get('position').get('y'),
                                               json_msg.get('position').get('z'),
                                               json_msg.get('position').get('quality'))
                    repository = TagLocationRepository()
                    repository.create(tag_location)
                elif topic[4] == 'data':
                    json_msg = json.loads(msg_text)
                    base64_message = json_msg.get('data')
                    message_bytes = base64.b64decode(base64_message)
                    print(message_bytes)
                    mybytes = bytearray(message_bytes)
                    print(mybytes)
                    count = mybytes[0]
                    print("\nCount: %d", count)
                    counter = mybytes[count*4+1]
                    print("\nCounter: %d", counter)

                    bytescounter = 1
                    for x in range(count):
                        address = mybytes[bytescounter+0] | (mybytes[bytescounter+1] & 0x000000FF) << 8
                        print("\nAddress: %x", hex(address))

                        distance = mybytes[bytescounter+2] | (mybytes[bytescounter+3] & 0x000000FF) << 8
                        print("\nDistance: %d", distance)
                        bytescounter = bytescounter + 4
                        distance = Distance(None,
                                            tag_id,
                                            str(hex(address)),
                                            str(distance),
                                            )
                        rep = DistanceRepository()
                        rep.create(distance)
        except Exception as e:
            print("An exception occurred")
            print(e)

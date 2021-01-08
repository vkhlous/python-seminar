
from MQTTListener import MQTTListener

from csv import reader
import base64
import json
import re
import simplejson as json3
from TagLocationRepository import TagLocationRepository

if __name__ == '__main__':
    mqtt_listener = MQTTListener("listener")
    mqtt_listener.connect()
    mqtt_listener.start_listening()
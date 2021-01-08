import json

from bson.objectid import ObjectId
import datetime
import paho.mqtt.client as mqtt
from TagLocationService import TagLocationService

counter = 0


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)
    global counter
    counter = counter + 1
    TagLocationService.process_message(message, counter)


def on_subscribe():
    print("Subscribed to queue")


def on_connect():
    print("Connected to MQTT broker")


class MQTTListener(object):

    def __init__(self, name):
        # initializing the MongoClient, this helps to
        self.broker_address = "127.0.0.1"  # Localhost
        self.mqtt_client = mqtt.Client(name, clean_session=True)

    def connect(self):
        self.mqtt_client.on_message = on_message
        self.mqtt_client.on_connect = on_connect()
        self.mqtt_client.on_subscribe = on_subscribe()
        self.mqtt_client.connect(host=self.broker_address, port=1883, keepalive=120)
        self.mqtt_client.username_pw_set(username="user", password="pass")
        self.mqtt_client.loop_start()

    def start_listening(self):
        self.mqtt_client.subscribe("dwm/node/+/uplink/data")
        self.mqtt_client.subscribe("dwm/node/+/uplink/location")
        while True:
            self.mqtt_client.loop_start()  # start the loop\

    def publish(self, tag_id, topic, json):
        self.mqtt_client.publish(topic="dwm/node/" + str(tag_id) + "/uplink/" + str(topic), payload=json, qos=0)

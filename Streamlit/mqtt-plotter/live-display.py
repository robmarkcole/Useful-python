import paho.mqtt.client as mqtt
import json
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import time


MQTT_BROKER = "10.42.0.130"
MQTT_TOPIC = "camera/numpy"

VIEWER_WIDTH = 600

cm_hot = plt.cm.get_cmap("hot")


def get_random_numpy():
    return np.random.randint(0, 100, size=(32, 32))

title = st.title('Title')
viewer = st.image(get_random_numpy(), width=VIEWER_WIDTH)

def process_mqtt_payload(payload: str):
    raw_json = json.loads(payload)
    timestamp = raw_json["timestamp"]
    frame = np.array(raw_json["frame"])
    return timestamp, frame

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    st.write(f"Connected with result code {str(rc)} to MQTT broker on {MQTT_BROKER}")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic != MQTT_TOPIC:
        return
    timestamp, frame = process_mqtt_payload(msg.payload.decode())
    frame -= frame.min()
    frame *= 255/frame.max()
    title.title(timestamp)
    viewer.image(frame.astype(int), width=VIEWER_WIDTH)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER)
client.subscribe(MQTT_TOPIC)

client.loop_forever()

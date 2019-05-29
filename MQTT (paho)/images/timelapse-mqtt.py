from time import sleep
from picamera import PiCamera
import paho.mqtt.client as mqtt

# broker = "localhost"
broker = "192.168.1.164"
topic = 'camera'
port = 1883

# Reqired callbacks
def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code {}".format(rc))
    if rc==0:
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

def on_publish(client, userdata, mid):
    print("mid: "+str(mid)) 

client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
#client.username_pw_set(username, password)
client.connect(broker, port=port)


FPS = 1 # the frames per second

camera = PiCamera()
sleep(2)

for filename in camera.capture_continuous('img{counter:03d}.jpg'):
    print('Captured %s' % filename)
    with open(filename, 'rb') as file:
        filecontent = file.read()
        byteArr = bytearray(filecontent)
        client.publish(topic, byteArr, qos=1)
    sleep(1/FPS) 

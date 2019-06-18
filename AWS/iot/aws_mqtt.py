"""
Class for publishing data to AWS MQTT broker.
"""
import os
import json

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

CWD = os.getcwd()
CERTIFICATE_DIR = "certificates"
CA_ROOT_CERT_FILE = f"{CWD}/{CERTIFICATE_DIR}/root-CA.crt"

# Thing key and cert are unique to each thing
THING_PRIVATE_KEY = f"{CWD}/{CERTIFICATE_DIR}/6556c4125c-private.pem.key"
THING_CERT_FILE = f"{CWD}/{CERTIFICATE_DIR}/6556c4125c-certificate.pem.crt"

MQTT_HOST = "a3t1w84m5sqa6l-ats.iot.eu-west-1.amazonaws.com"

class aws_mqtt_broker():
    def __init__(self, client_id : str = ""):
        self.myMQTTClient = AWSIoTMQTTClient(client_id)
        self.myMQTTClient.configureEndpoint(MQTT_HOST, 8883)
        self.myMQTTClient.configureCredentials(CA_ROOT_CERT_FILE, 
                                               THING_PRIVATE_KEY, 
                                               THING_CERT_FILE)
        self.myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec
        if self.myMQTTClient.connect():
            print("Connected to AWS MQTT broker")
        else:
            print("Connection to AWS MQTT broker failed")
    
    def publish(self, topic : str, message : str):
        payload = json.dumps({'data': message}) # Wrap the message in a payload template
        
        if self.myMQTTClient.publish(topic, payload, QoS=0):
            print(f"Published message : {message} | topic : {topic}")
        else:
            print(f"Failed to publish message : {message}")

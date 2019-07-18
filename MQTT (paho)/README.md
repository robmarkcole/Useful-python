# Brokers
## Mosquitto - basic broker - RECOMMENDED
* Use the Eclipse broker mosquitto at https://github.com/eclipse/mosquitto 
* On mac `brew install mosquitto`
* To have the broker start automatically on Mac startup: `brew services start mosquitto`
* Or, if you don't want/need a background service you can just run: `mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf`
* **For desktop app I like [MQTT Client on Mac OS](https://itunes.apple.com/gb/app/mqtt-client/id1223420119?mt=12)**

## HiveMQ - broker + UI for broker management - OVERKILL
* Run a broker and web UI using a docker image at https://hub.docker.com/r/hivemq/hivemq3/ (don't confuse with `hivemq4` which is the Enterprise container)
* Run with `docker run -p 8080:8080 -p 1883:1883 hivemq/hivemq3` and head to http://localhost:8080/
* default Username: admin
* default Password: hivemq
* Get a nice web UI for messages -> clone https://github.com/hivemq/hivemq-mqtt-web-client and open `index.html`
* Can [deploy on AWS](https://www.hivemq.com/downloads/aws/)

## Paho
* `pip3 install paho-mqtt`
* https://github.com/eclipse/paho.mqtt.python
* The examples in the paho repo are very useful
* [`message_callback_add()`](https://github.com/eclipse/paho.mqtt.python#message_callback_add) can be used to register callbacks to specific topics
* [Example connecting to AWS IOT](https://www.hackster.io/mariocannistra/python-and-paho-for-mqtt-with-aws-iot-921e41) -> regular MQTT with TLS certificates 

# Useful links
* [mqttfx - another desktop app](https://mqttfx.jensd.de/index.php)
* [mosquitto in docker on a synology](https://philhawthorne.com/setting-up-a-local-mosquitto-server-using-docker-for-mqtt-communication/)
* [Sending and Receiving Pictures From a Raspberry Pi via MQTT](https://developer.ibm.com/recipes/tutorials/sending-and-receiving-pictures-from-a-raspberry-pi-via-mqtt/)

## Homie
MQTT doesn’t define the structure and content of these messages and their relation. An IoT device publishes data and provides interaction possibilities but a controlling entity will need to be specifically configured to be able to interface with the device. The Homie convention defines a standardized way of how IoT devices and services announce themselves and their data on the MQTT broker. Homies topic layout follows the pattern `homie/device/node/property`
* [homieiot mqtt convention](https://homieiot.github.io/)
* [microhomie](https://github.com/microhomie/microhomie) -> homie for micropython
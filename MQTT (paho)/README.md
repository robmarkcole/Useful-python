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

## Chrome apps
* [MQTT lens](https://chrome.google.com/webstore/detail/mqttlens/hemojaaeigabkbcookmlgmdigohjobjm?hl=en)
* [MQTTBox](https://chrome.google.com/webstore/detail/mqttbox/kaajoficamnjijhkeomgfljpicifbkaf?utm_source=chrome-ntp-launcher)

# Useful links
* [mqttfx - another desktop app](https://mqttfx.jensd.de/index.php)
* [homieiot mqtt convention](https://homieiot.github.io/)
* [mosquitto in docker on a synology](https://philhawthorne.com/setting-up-a-local-mosquitto-server-using-docker-for-mqtt-communication/)
* [Sending and Receiving Pictures From a Raspberry Pi via MQTT](https://developer.ibm.com/recipes/tutorials/sending-and-receiving-pictures-from-a-raspberry-pi-via-mqtt/)
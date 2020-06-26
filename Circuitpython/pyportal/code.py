import board
import busio
from digitalio import DigitalInOut
import neopixel
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_wifimanager
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# If you are using a board with pre-defined ESP32 Pins:
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)
status_light = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2) # Uncomment for Most Boards
wifi = adafruit_esp32spi_wifimanager.ESPSPI_WiFiManager(esp, secrets, status_light)

mqtt_topic = 'test'

def connect(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print('Connected to MQTT Broker!')
    print('Flags: {0}\n RC: {1}'.format(flags, rc))

def subscribe(client, userdata, topic, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print('Subscribed to {0} with QOS level {1}'.format(topic, granted_qos))

def publish(client, userdata, topic, pid):
    # This method is called when the client publishes data to a feed.
    print('Published to {0} with PID {1}'.format(topic, pid))

def message(client, topic, message):
    """Method callled when a client's subscribed feed has a new
    value.
    :param str topic: The topic of the feed with a new value.
    :param str message: The new value
    """
    print('New message on topic {0}: {1}'.format(topic, message))

# Connect to WiFi
wifi.connect()
print("Connected to", str(esp.ssid, 'utf-8'), "\tRSSI:", esp.rssi)
print("My IP address is", esp.pretty_ip(esp.ip_address))
    
# Initialize MQTT interface with the esp interface
MQTT.set_socket(socket, esp)
# Set up a MiniMQTT Client
client =  MQTT.MQTT(broker = '192.168.1.164', port=1883)

# Connect callback handlers to client
client.on_connect = connect
client.on_subscribe = subscribe
client.on_publish = publish
client.on_message = message

print('Attempting to connect to %s'%client.broker)
client.connect()

print('Subscribing to %s'%mqtt_topic)
client.subscribe(mqtt_topic)

print('Publishing to %s'%mqtt_topic)
client.publish(mqtt_topic, 'Hello from pyportal!')

#while True:
    # Poll the message queue
    #client.loop()

while True:
    try:
        client.loop()
    except (ValueError, RuntimeError) as e:
        print("Failed to get data, retrying\n", e)
        wifi.reset()
        client.reconnect()
        continue
    time.sleep(1)
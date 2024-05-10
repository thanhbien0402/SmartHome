import sys
import time 
import random
from Adafruit_IO import MQTTClient
# from simple_ai import *
from uart import *

AIO_FEED_IDs = ["nutnhan1", 'nutnhan2']
AIO_USERNAME = "bcthanh"
AIO_KEY = "aio_FZTN68tVswKnsf3Fnz5R3j6BzVmm"

def connected(client):
    print("Ket noi thanh cong...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong...")

def disconnected(client):
    print("Ngat ket noi...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)
    if feed_id == "nutnhan1":
        if payload == "0":
            writeData(1)
        else:
            writeData(2)
    if feed_id == "nutnhan2":
        if payload == "0":
            writeData(3)
        else:
            writeData(4)


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

# counter = 10
# sensor_type = 0

counter_ai = 2
ai_result = ""
prev_ai_result = ""

while True:
    # counter = counter - 1
    # if counter <= 0:
    #     counter = 10

    #     print("Random data is publishing...")
    #     if sensor_type == 0:
    #         temp = random.randint(10, 70)
    #         print("Temperature: ", temp)
    #         client.publish("cambien1", temp)
    #         sensor_type = 1
    #     elif sensor_type == 1:
    #         humi = random.randint(0, 100)
    #         print("Humidity: ",  humi)
    #         client.publish("cambien2", humi)
    #         sensor_type = 2
    #     elif sensor_type == 2:
    #         light = random.randint(30, 500)
    #         print("Light: ", light)
    #         client.publish("cambien3", light)
    #         sensor_type = 0

    # counter_ai = counter_ai - 1
    # if counter_ai <= 0:
    #     counter_ai = 2
    #     prev_ai_result = ai_result
    #     ai_result = image_detector()
    #     print("AI Output: ", ai_result)
    #     if prev_ai_result != ai_result:
    #         client.publish("ai", ai_result)

    readSerial(client)

    time.sleep(1)

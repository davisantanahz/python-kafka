import os
from kafka import KafkaConsumer
from json import loads

class Consumer():
    def __init__(self):
        host =  os.getenv('HOST_KAFKA')
        consumer = KafkaConsumer('test-topic', bootstrap_servers=[ host + ':9092'])

        for message in consumer:
            message = message.value
            print('{} added to '.format(message))
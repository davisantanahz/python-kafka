from kafka import KafkaConsumer
# from kafka import TopicPartition
from json import loads

# consumer = KafkaConsumer('test-topic', bootstrap_servers=['kafka:9092'])

class Consumer():
    def __init__(self):
        consumer = KafkaConsumer('test-topic', bootstrap_servers=['kafka:9092'])

        for message in consumer:
            message = message.value
            print('{} added to '.format(message))
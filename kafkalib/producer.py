import os
from kafka import KafkaProducer
import json 

class Producer():
    def __init__(self):
        host =  os.getenv('HOST_KAFKA')
        producer = KafkaProducer(bootstrap_servers= host + ':9092')
        producer.send('test-topic', b'some_message_bytes')
        producer.flush()
        producer.close()
        # producer_json = KafkaProducer(bootstrap_servers='localhost:9092',
        #                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        # producer_json.send('test-topic', {'foo': 'bar'})
        # producer_json.flush()
        # producer_json.close()
        
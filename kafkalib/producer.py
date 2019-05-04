from kafka import KafkaProducer
import json 

class Producer():
    def __init__(self):
        producer = KafkaProducer(bootstrap_servers='kafka:9092')
        producer.send('test-topic', b'some_message_bytes')
        producer.flush()
        producer.close()
        # producer_json = KafkaProducer(bootstrap_servers='localhost:9092',
        #                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        # producer_json.send('test-topic', {'foo': 'bar'})
        # producer_json.flush()
        # producer_json.close()
        
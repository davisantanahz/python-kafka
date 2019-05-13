import os
from flask import Flask
from kafkalib import producer 
from kafkalib import consumer

app = Flask(__name__)

host =  os.getenv('HOST_KAFKA')

@app.route('/')
def hello_world():
    return 'Hello world! Host: ' + host


@app.route('/kafka')
def run_kafka():
    return 'Verify run kafka!'


@app.route('/producer')
def run_producer():
    return producer.Producer()


@app.route('/consumer')
def run_consumer():
    return consumer.Consumer()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
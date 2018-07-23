# Dependencies
import time
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError

class kafka_producer:
    broker_ip = '172.31.87.138'
    port = 9092
    topic = "test-python1"
    producer = None

    # Initialize the class object
    def __init__(self, new_broker_ip, new_port):
        self.server_ip = new_broker_ip
        self.port = new_port

        self.producer = self.initialize_producer()

    # Set up a producer
    def initialize_producer(self):
        broker = self.broker_ip + ":" + self.port
        print(broker)
        producer = KafkaProducer(bootstrap_servers='172.31.87.138:9092', value_serializer=lambda m: json.dumps(m).encode('ascii'))
        return producer

    # Send any json object to topic
    def send_data_object(self, data_object):
        print(self.broker_ip + ":" + self.port)
        self.producer.send('test-python1', {'key': 'value'})

    # Set current topic
    def set_topic(self, new_topic):
        self.topic = new_topic

    # Get current topic
    def get_topic(self):
        return self.topic
#!/usr/bin/env python
import threading, logging, time
import multiprocessing
import json 
import sys
import configparser
from kafka import KafkaProducer

class Producer(threading.Thread):

    data_to_send = {}
    topic = ""
    broker = ""

    def __init__(self, new_broker, new_topic, new_data):
        threading.Thread.__init__(self)
        self.data_to_send = new_data
        self.topic = new_topic
        self.broker = new_broker
        self.stop_event = threading.Event()
        
    def stop(self):
        self.stop_event.set()

    def run(self):
        # producer = KafkaProducer(bootstrap_servers='172.31.87.138:9092')
        producer = KafkaProducer(bootstrap_servers=self.broker, value_serializer=lambda m: json.dumps(m).encode('ascii'))

        while not self.stop_event.is_set():
            producer.send(self.topic, self.data_to_send)
            time.sleep(1)

        producer.close()

    
        
def main():
    
    # Parse config file
    config = configparser.ConfigParser()
    config.read("kafka.cfg")

    broker = config['kafka']['host_broker']
    topic = config['kafka']['topic'] 
    dataString = sys.argv
    data = json.loads(dataString)

    tasks = [
        Producer(broker, topic, data),
    ]

    for t in tasks:
        t.start()

    time.sleep(1)
    
    for task in tasks:
        task.stop()

    for task in tasks:
        task.join()
        
        
if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    main()
    
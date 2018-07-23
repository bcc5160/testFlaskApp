#!/usr/bin/env python
import threading, logging, time
import multiprocessing
import json
import configparser
from kafka import KafkaConsumer
import sys 

class Consumer(multiprocessing.Process):

    topic = ""
    broker = ""

    def __init__(self, new_broker, new_topic):

        self.topic = new_topic
        self.broker = new_broker

        multiprocessing.Process.__init__(self)
        self.stop_event = multiprocessing.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=self.broker,
                                 auto_offset_reset='earliest',
                                 consumer_timeout_ms=1000,
                                 value_deserializer=lambda m: json.loads(m.decode('ascii')))
        consumer.subscribe([self.topic])

        while not self.stop_event.is_set():
            for message in consumer:
                print(message)
                if self.stop_event.is_set():
                    break

        consumer.close()


def main():
     # Parse config file
    config = configparser.ConfigParser()
    config.read("kafka.cfg")

    broker = config['kafka']['host_broker']
    topic = config['kafka']['topic'] 

    tasks = [
        Consumer(broker, topic)
    ]

    for t in tasks:
        t.start()

    time.sleep(10)
    
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
from kafka_interface import kafka_producer
import json 

BROKER = "172.31.87.138" 
PORT = "9092"

producer = kafka_producer(BROKER, PORT)

producer.send_data_object({"jkey": "val"})
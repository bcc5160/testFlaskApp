# Dependencies
import os
import subprocess
import json

def main():
    for i in range(0, 4):
        data = {}
        data["Number " + str(i)] = str(i)
        json_data = json.dumps(data) 
        print(json_data)
        cmd = "python3 kafka_producer_interface.py '" + json_data + "'"
        os.system(cmd)

main()
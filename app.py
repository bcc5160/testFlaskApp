from flask import Flask, request
import os 
import docker
from docker import Client
import json 

# Global Variables
DOCKER_REPO = '34.231.172.160'
BASE_NAME = 'base'
BASE_TAG = 'v2'

# Docker Setup
docker_client = Client(base_url='http://localhost:2376/')

app = Flask(__name__)

@app.route('/newApp', methods = ['POST'])
def new_app():
    data = request.get_json()
    print(data['new_app'])
    new_name = data['new_app']

    print(type(str(new_name + ':' + BASE_TAG)))
    new_name = new_name.replace(" ", "_")

    base_app_image = DOCKER_REPO + '/' + BASE_NAME + ':' + BASE_TAG
    new_app_image = DOCKER_REPO + '/' + str(new_name)

    docker_client.pull(base_app_image + ':' + BASE_TAG)
    docker_client.tag(base_app_image, new_app_image, BASE_TAG)
    
    response = [line for line in docker_client.push(new_app_image, stream=True)]
    
    # Create a kafka topic for app
    os.system("bin/kafka-create-topic.sh --zookeeper localhost:2181 --replica 1 --partition 1 --topic " + str(new_name))

    # Create consumer folder with config for topic
    os.system("cp -r /opt/BigData/BaseApp /opt/BigData/Apps/" + new_app_image)

    # Createconfig
    f = open(new_app_image +".cfg","w+")
    f.write("[kafka]\nhost_broker=172.31.87.138:9092\ntopic=" + new_app_image)

    print(response)
    return new_app_image + ':' + BASE_TAG


@app.route('/up', methods = ['GET'])
def test_server():
    return "OK."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)                                                   
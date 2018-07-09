from flask import Flask, request
import os 
import docker

# Global Variables
DOCKER_REPO = '34.231.172.160'
BASE_NAME = 'base'
BASE_TAG = 'v2'

# Docker Setup
docker_client = docker.from_env()

app = Flask(__name__)

@app.route('/newApp', methods = ['POST'])
def new_app():
    new_name = request.get_json()
    
    docker_client.images.pull(DOCKER_REPO + "/" + BASE_NAME + ":" + BASE_TAG)
    
    image = docker_client.images.get(DOCKER_REPO + "/" + BASE_NAME + ":" + BASE_TAG)
    image.tag(DOCKER_REPO + "/" + str(new_name) + ":" + BASE_TAG)

    docker_client.images.push(DOCKER_REPO + "/" + str(new_name) + ":" + BASE_TAG)

    return str(new_name) + ' was created.'



@app.route('/up', methods = ['GET'])
def test_server():
    return "OK."

if __name__ == '__main__':
    app.run(debug=True)


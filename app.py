from flask import Flask
import os 
import docker

# Docker Setup
docker_client = docker.from_env()

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'
    # return docker_client.images.list()

if __name__ == '__main__':
    app.run(debug=True)


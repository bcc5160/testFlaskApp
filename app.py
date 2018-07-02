from flask import Flask
import os 
import docker

app = Flask(__name__)

@app.route('/')
def index():
    
    return 'index2'

if __name__ == '__main__':
    app.run(debug=True)


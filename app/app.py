from flask import Flask
from prometheus_client import start_http_server, Summary
import random
import time

app = Flask(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()
def hello():
    time.sleep(random.random())
    return "Hello, this is monitored!"

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

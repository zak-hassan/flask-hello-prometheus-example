from flask import Flask
from prometheus_client import start_http_server
from prometheus_client import Counter

app = Flask(__name__)

REQUESTS = Counter('hello_worlds_total',
        'Hello Worlds requested.')

 
@app.route("/")
def hello():
    REQUESTS.inc()
    return "Hello World!"
 
if __name__ == "__main__":
    start_http_server(8000)
    app.run()

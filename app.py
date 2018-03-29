from flask import Flask
from prometheus_client import start_http_server,Summary,Counter,Gauge

app = Flask(__name__)

TOTAL_REQ = Counter('hello_worlds_total','Hello Worlds requested.')
LAST_TIME = Gauge('hello_world_last_time_seconds','The last time a Hello World was served.')

@app.route("/")
def hello():
    LAST_TIME.set_to_current_time()
    TOTAL_REQ.inc()
    return "Hello World!"

if __name__ == "__main__":
    start_http_server(8000)
    app.run()

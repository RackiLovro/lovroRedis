import redis
import os
from flask import Flask

app = Flask(__name__)
redis_host = "redis"
redis_port = int(os.environ.get("REDIS_PORT", 6379))


# increment the counter by one
@app.route("/")
def increment():
    r.incr("visitCounter")
    print(r.get("visitCounter"))
    return "Incrementing counter"


# reset the counter to zero
@app.route("/reset")
def reset():
    r.set("visitCounter", 0)
    return "Reseting counter to 0"


if __name__ == "__main__":
    r = redis.Redis(host="redis", port=redis_port, decode_responses=True)
    app.run(host="0.0.0.0")

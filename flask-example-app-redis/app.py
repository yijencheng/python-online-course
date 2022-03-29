
from flask import Flask
from flask_cors import CORS, cross_origin
import redis

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Redis
app.config['REDIS_URL'] = "redis://localhost:6379"
redis_client = redis.Redis(host='localhost', port=6379, db=0)


#Warning: you should either name the file "app.py", or you shoud provide FLASK_APP env. 
@app.route("/api/test", methods=["GET", "POST"])
def test():
    return {
        "status":200,
        "message":"Success"
    }


@app.route("/api/get_data", methods=["GET"])
def get_data():
    redis_client.set("foo","bar")
    return {
        "status":200,
        "data":redis_client.get("foo").decode("utf-8")
    }


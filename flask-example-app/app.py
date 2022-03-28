from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api/test", methods=["GET", "POST"])
def test():
    return {
        "status":200,
        "message":"Success"
    }

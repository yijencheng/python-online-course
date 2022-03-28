
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Warning: you should either name the file "app.py", or you shoud provide FLASK_APP env. 
@app.route("/api/test", methods=["GET", "POST"])
def test():
    return {
        "status":200,
        "message":"Success"
    }

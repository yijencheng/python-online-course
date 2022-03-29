
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#postgres
POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'mydb',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
db = SQLAlchemy(app)

#Warning: you should either name the file "app.py", or you shoud provide FLASK_APP env. 
@app.route("/api/test", methods=["GET", "POST"])
def test():
    return {
        "status":200,
        "message":"Success"
    }


@app.route("/api/get_data", methods=["GET"])
def get_data():
    with db.engine.connect() as connection:
        t = text("SELECT * FROM users WHERE id=:user_id")
        result = connection.execute('SELECT * FROM test LIMIT 10')
    
    data = []
    for r in result:
        obj = {
            "id": r['id'],
            "name": r['name']
        }
        data.append(obj)

    return {
        "status":200,
        "data":data
    }


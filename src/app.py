from flask import Flask, render_template, request, jsonify
import mymodel as mm
import json
import requests
import socket
import time
from datetime import datetime
import loaddata as ld
import cleaning_script as cs
app = Flask(__name__)
PORT = 5353
REGISTER_URL = "http://10.5.3.92:5000/register"
DATA = []
TIMESTAMP = []


# home page
@app.route('/', methods=['GET'])
def index():
    return render_template('welcome.html')

@app.route('/score', methods=['POST'])
def score():
    raw_data = request.json
    ld.load_raw(raw_data, db)
    clean_json = cs.clean(raw_data)
    obj_id = ld.load_clean(clean_json, db)
    prediction = model.transform_predict(clean_json)
    ld.load_pred(prediction, obj_id, db)

@app.route('/load', methods=['GET'])
def load():
    data = ld.dump_collection(db, 'pred_t')
    return data

def register_for_ping(ip, port):
    registration_data = {'ip': ip, 'port': port}
    requests.post(REGISTER_URL, data=registration_data)


if __name__ == '__main__':
    # Register for pinging service
    ip_address = socket.gethostbyname(socket.gethostname())
    print "attempting to register %s:%d" % (ip_address, PORT)
    register_for_ping(ip_address, str(PORT))

    db = ld.connect_to_db()
    model = mm.MyModel()
    model.load_model('finalized_model.pkl')
    app.run(host='0.0.0.0', port=8080, debug=True)

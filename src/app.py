from flask import Flask, render_template, request, jsonify
import clean_and_predict as cap
from flask import Flask, request, render_template
import json
import requests
import socket
import time
from datetime import datetime
import loaddata as ld
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
    clean_json = cleaner.clean_data(raw_data)
    obj_id = ld.load_clean(clean_json, db)
    prediction = model.transform_predict(clean_json)
    ld.load_pred(prediction, obj_id, db)

def register_for_ping(ip, port):
    registration_data = {'ip': ip, 'port': port}
    requests.post(REGISTER_URL, data=registration_data)


if __name__ == '__main__':

    # Register for pinging service
    ip_address = socket.gethostbyname(socket.gethostname())
    print "attempting to register %s:%d" % (ip_address, PORT)
    register_for_ping(ip_address, str(PORT))


    db = ld.connect_to_db()
    cleaner = cap.DataCleaner()
    model = cap.MyModel()
    model.load_model('model.pkl')
    app.run(host='0.0.0.0', port=8080, debug=True)

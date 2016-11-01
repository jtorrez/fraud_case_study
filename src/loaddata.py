from __future__ import division
from math import sqrt
from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import json

# Loads data
#

# Load raw data - input
#

def connect_to_db():
    conn = MongoClient('mongodb://localhost:27017/')
    db = conn.fraud
    return db

def load_raw(i,db):
    raw_t = db.raw_t
    data = json.loads(i)
    raw_t.insert(data)

def load_clean(i,db):
    clean_t = db.clean_t
    data = json.loads(i)
    return clean_t.insert(data)

def load_pred(pred_tup,clean_obj_id,db):
    # pred_tup = tuple of probablity
    data = [{"probability":pred_tup[0],'label': pred_tup[1], 'cleandata_ob_id': clean_obj_id}]
    n = json.dumps(data)
    pred_t = db.pred_t
    pred_t.insert(n)

if __name__ == '__main__':
    #conn = MongoClient('mongodb://localhost:27017/')
    #db = conn.fraud
    db = connect_to_db()
    print db
    data=[{"org_name": "DREAM Project Foundation", "name_length": 51}]
    n = json.dumps(data)
    load_raw(n, db)

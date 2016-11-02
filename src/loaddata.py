from pymongo import MongoClient
import json

#
# Ineraction:
#   Call connect_to_db() to return db
#   Call load_raw to save data from POST comment
#   Call load_clean to save cleaned data
#   Call load_predict to save prediction output and object id from cleaned data


def connect_to_db():
    """
    Connects to database
    NOTE: if database does not exist, one will be created

    Parameters
    ----------
    None

    Returns
    -------
    db = database fraud
    """
    conn = MongoClient('mongodb://localhost:27017/')
    db = conn.fraud
    return db

def load_raw(i,db):
    """
    Loads raw json file into mongodb colllection

    Parameters
    ----------
    i: JSON str
        JSON object of raw data sent by POST request

    Returns
    -------
    None

    """
    raw_t = db.raw_t
    data = json.loads(i)
    raw_t.insert(data)

def load_clean(i,db):
    """
    Loads cleaned json file into mongodb collection

    Parameters
    ----------
    i: JSON str
        JSON object of raw data sent by POST request

    Returns
    -------
    Object id from inserted row
    """
    clean_t = db.clean_t
    data = json.loads(i)
    return clean_t.insert(data)

def load_pred(pred_tup,clean_obj_id,db):
    """
    Loads predictions into mongodb collection

    Parameters
    ----------
    pred_tup: tuple containing (probability,risk label)
                output of model
    clean_obj_id: object id from clean data in mongo collection

    Returns
    -------
    None
    """
    # pred_tup = tuple of probablity
    data = [{"probability":pred_tup[0],'label': pred_tup[1], 'cleandata_ob_id': clean_obj_id}]
    n = json.dumps(data)
    pred_t = db.pred_t
    pred_t.insert(n)

if __name__ == '__main__':
    db = connect_to_db()
    data=[{"org_name": "DREAM Project Foundation", "name_length": 51}]
    n = json.dumps(data)
    load_raw(n, db)

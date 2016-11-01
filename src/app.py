from flask import Flask, render_template, request, jsonify
import clean_and_predict as cap
#import loaddata as ld
app = Flask(__name__)

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

if __name__ == '__main__':
    db = ld.connect_to_db()
    cleaner = cap.DataCleaner()
    model = cap.MyModel()
    model.load_model('model.pkl')
    app.run(host='0.0.0.0', port=8080, debug=True)

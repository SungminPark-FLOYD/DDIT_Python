from flask import Flask
from flask.helpers import make_response
from flask.json import jsonify
from flask.globals import request


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello flask'

@app.route('/ajax', methods = ["GET", "POST"])
def ajax():
    data = request.get_json();
    print(data['menu'])
    res = make_response(data, 200)
    return res

@app.route('/fetch', methods = ["GET", "POST"])
def fetch():
    data = request.get_json();
    print(data['menu'])
    res = make_response(jsonify({'result' : 'success'}), 200)
    return res

@app.route('/axios', methods = ["GET", "POST"])
def axios():
    meta = request.get_json();
    print(meta['data']['menu'])
    res = make_response(jsonify({'result' : 'success'}), 200)
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
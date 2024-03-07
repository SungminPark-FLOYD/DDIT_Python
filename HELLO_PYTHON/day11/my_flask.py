from flask import Flask
from flask.globals import request
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello flask'


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
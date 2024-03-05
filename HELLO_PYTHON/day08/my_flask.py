from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day08.dao_emp import DaoEmp

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello flask'

@app.route('/param')
def param():
    #dic = request.args["menu"]
    menu = request.args.get('menu', default='탕수육')
    return 'param: {}'.format(menu)

@app.route('/post', methods=['GET', 'POST'])
def post():
    menu = request.form['menu']
    return 'post : {}'.format(menu)

@app.route('/forw')
def forw():
    a = "홍길동"
    b = ["전우치", "임꺽정"]
    c = [
        {'e_id':1, 'e_name':1, 'gen':1, 'addr':1},
        {'e_id':2, 'e_name':2, 'gen':2, 'addr':2}
    ]
    return render_template('forw.html', name=a, list=b, c=c)

@app.route('/emp')
def emp():
    de = DaoEmp()
    list = de.selectList()
    
    return render_template('emp.html', list=list)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
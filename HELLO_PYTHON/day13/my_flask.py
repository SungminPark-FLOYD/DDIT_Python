from flask import Flask
from flask.helpers import make_response, redirect
from flask.globals import request
from day13.dao_emp import DaoEmp
from flask.json import jsonify


app = Flask(__name__)

@app.route('/')
def hello():
    return redirect('/static/emp.html')

@app.route('/empList', methods = ["GET", "POST"])
def empList():
    de = DaoEmp()
    list = de.selectList()  
    return jsonify(list = list)

@app.route('/empone', methods = ["GET", "POST"])
def empone():   
    data = request.get_json() 
    e_id = data['e_id']

    de = DaoEmp()
    vo = de.selectOne(e_id)
    
    return jsonify(vo=vo)

@app.route('/empadd', methods = ["GET", "POST"])
def empadd():    
    data = request.get_json() 
    print(data)
    e_id = data['e_id']   
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    
    return jsonify(cnt = cnt)

@app.route('/empmod', methods = ["GET", "POST"])
def empmod():    
    data = request.get_json() 
    print(data)
    e_id = data['e_id']   
    e_name = data['e_name']
    gen = data['gen']
    addr = data['addr']
    
    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
    
    return jsonify(cnt = cnt)

@app.route('/empdel', methods = ["GET", "POST"])
def empdel():    
    data = request.get_json() 
    print(data)
    e_id = data['e_id']   
    
    de = DaoEmp()
    cnt = de.delete(e_id)
    
    return jsonify(cnt = cnt)

@app.route('/ajax', methods = ["GET", "POST"])
def ajax():
    data = request.get_json();
    print(data['menu'])
    res = make_response(data, 200)
    return res

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
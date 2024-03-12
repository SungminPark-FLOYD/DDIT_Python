from flask import Flask
from flask.helpers import make_response, redirect
from flask.globals import request
from flask.json import jsonify
from day14.dao_exam import DaoExam


app = Flask(__name__)

@app.route('/')
def hello():
    return redirect('/static/exam.html')

@app.route('/examList', methods = ["GET", "POST"])
def examList():
    de = DaoExam()
    list = de.selectList()  
    return jsonify(list = list)

@app.route('/examone', methods = ["GET", "POST"])
def examone():   
    data = request.get_json() 
    e_id = data['e_id']

    de = DaoExam()
    vo = de.selectOne(e_id)
    
    return jsonify(vo=vo)

@app.route('/examadd', methods = ["GET", "POST"])
def examadd():    
    data = request.get_json() 
    print(data)
    e_id = data['e_id']   
    e_que = data['e_que']   
    ans1 = data['ans1']   
    ans2 = data['ans2']   
    ans3 = data['ans3']   
    ans4 = data['ans4']   
    ans = data['ans']   

    de = DaoExam()
    cnt = de.insert(e_id,e_que,ans1,ans2,ans3,ans4,ans)
    
    return jsonify(cnt = cnt)
@app.route('/exammod', methods = ["GET", "POST"])
def exammod():    
    data = request.get_json() 
    print(data)
    e_id = data['e_id']   
    e_que = data['e_que']   
    ans1 = data['ans1']   
    ans2 = data['ans2']   
    ans3 = data['ans3']   
    ans4 = data['ans4']   
    ans = data['ans'] 
    
    de = DaoExam()
    cnt = de.update(e_id,e_que,ans1,ans2,ans3,ans4,ans)
    
    return jsonify(cnt = cnt)

@app.route('/examdel', methods = ["GET", "POST"])
def examdel():    
    data = request.get_json() 
    print(data)
    e_id = data['e_id']   
    
    de = DaoExam()
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
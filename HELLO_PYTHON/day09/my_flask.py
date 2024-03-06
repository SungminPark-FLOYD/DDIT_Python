from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day09.dao_emp import DaoEmp


app = Flask(__name__)

@app.route('/')
@app.route('/emp_list')
def emp_list():
    de = DaoEmp()
    list = de.selectList()
    
    return render_template('emp_list.html', list=list)

@app.route('/emp_detail')
def emp_detail():
    e_id = request.args.get('e_id', type = str)      
    de = DaoEmp()
    vo = de.selectOne(e_id)
    
    return render_template('emp_detail.html', vo=vo)

@app.route('/emp_mod')
def emp_mod():
    e_id = request.args.get('e_id', type = str)      
    de = DaoEmp()
    vo = de.selectOne(e_id)
    
    return render_template('emp_mod.html', vo=vo)


@app.route('/emp_mod_act', methods=['GET', 'POST'])
def emp_update():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']

    de = DaoEmp()
    cnt = de.update(e_id, e_name, gen, addr)
       
    return render_template('emp_mod_act.html', cnt=cnt)



@app.route('/emp_delete', methods=['GET', 'POST'])
def emp_delete():
    e_id = request.form['e_id']    

    de = DaoEmp()
    cnt = de.delete(e_id)
           
    return render_template('emp_mod_act.html', cnt=cnt)

@app.route('/emp_add')
def emp_add():    
    return render_template('emp_add.html')

@app.route('/emp_add_act', methods=['GET', 'POST'])
def emp_insert():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']

    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
       
    return render_template('emp_mod_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
    
    
    
    
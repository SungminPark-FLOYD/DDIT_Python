from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day10.dao_mem import DaoMem

app = Flask(__name__)

@app.route('/')
@app.route('/mem_list')
def mem_list():
    dm = DaoMem()
    list = dm.selectList()
    
    return render_template('mem_list.html', list=list)


@app.route('/mem_detail')
def mem_detail():
    m_id = request.args.get('m_id', type = str)      
    dm = DaoMem()
    vo = dm.selectOne(m_id)
    
    return render_template('mem_detail.html', vo=vo)

@app.route('/mem_mod')
def mem_mod():
    m_id = request.args.get('m_id', type = str)      
    dm = DaoMem()
    vo = dm.selectOne(m_id)
    
    return render_template('mem_mod.html', vo=vo)


@app.route('/mem_mod_act', methods=['GET', 'POST'])
def mem_update():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    tel = request.form['tel']
    email = request.form['email']

    dm = DaoMem()
    cnt = dm.update(m_id, m_name, tel, email)
       
    return render_template('mem_mod_act.html', cnt=cnt)



@app.route('/mem_delete', methods=['GET', 'POST'])
def mem_delete():
    m_id = request.form['m_id']    

    dm = DaoMem()
    cnt = dm.delete(m_id)
           
    return render_template('mem_mod_act.html', cnt=cnt)

@app.route('/mem_add')
def mem_add():    
    return render_template('mem_add.html')

@app.route('/mem_add_act', methods=['GET', 'POST'])
def mem_insert():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    tel = request.form['tel']
    email = request.form['email']

    dm = DaoMem()
    cnt = dm.insert(m_id, m_name, tel, email)
       
    return render_template('mem_mod_act.html', cnt=cnt)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
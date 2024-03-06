import cx_Oracle

class DaoMem:
    def __init__(self):
        self.con = cx_Oracle.connect('python/py@localhost:1521/xe')
        self.cur = self.con.cursor()
   
    def selectList(self):
        self.cur.execute("select * from mem order by m_id")
        rows = self.cur.fetchall()
        
        list = []
        for i in rows:
            list.append({'m_id':i[0], 'm_name':i[1], 'tel':i[2], 'email':i[3]})
            
        return list
     
    def selectOne(self, m_id):
        sql = f"""
            select * 
            from mem 
            where m_id = '{m_id}' 
            order by m_id
        """
        self.cur.execute(sql)
        row = self.cur.fetchone()
        vo = {'m_id':row[0], 'm_name':row[1], 'tel':row[2], 'email':row[3]}
            
        return vo 
           
    def insert(self, m_id,m_name,tel,email):
        sql = f"""
            insert into mem(m_id,m_name,tel,email)
            values('{m_id}','{m_name}','{tel}','{email}')
        """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        
        print(cnt)
        return cnt
    
    def delete(self, m_id):
        sql = f"""
            delete from mem where m_id = '{m_id}'
        """
        
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        
        return cnt
    
    def update(self, m_id,m_name,tel,email):
        sql = f"""
            update mem set
            m_name = '{m_name}',
            tel = '{tel}',
            email = '{email}'
            where m_id = '{m_id}'
        """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
                
        return cnt

    def __del__(self):
        self.cur.close()    
        self.con.close()

if __name__== '__main__':
    de = DaoMem()
    # emp1 = de.selectList()
    # emp2 = de.selectOne('4')
    # cnt = de.insert('4','4','4','4')
    # cnt = de.update('4', '5', '5', '5')
    # cnt = de.delete('4')
    # print(cnt)

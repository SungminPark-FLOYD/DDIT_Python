import cx_Oracle

class DaoEmp:
    def __init__(self):
        self.con = cx_Oracle.connect('python/py@localhost:1521/xe')
        self.cur = self.con.cursor()
   
    def selectList(self):
        self.cur.execute("select * from emp order by e_id desc")
        rows = self.cur.fetchall()
        list = []
        for i in rows:
            list.append({'e_id':i[0], 'e_name':i[1], 'gen':i[2], 'addr':i[3]})
            
        return list
     
    def selectOne(self, e_id):
        sql = f"""
            select * 
            from emp 
            where e_id = '{e_id}' 
            order by e_id
        """
        self.cur.execute(sql)
        row = self.cur.fetchone()
        vo = {'e_id':row[0], 'e_name':row[1], 'gen':row[2], 'addr':row[3]}
            
        return vo 
           
    def insert(self, e_id,e_name,gen,addr):
        sql = f"""
            insert into emp(e_id,e_name,gen,addr)
            values('{e_id}','{e_name}','{gen}','{addr}')
        """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        
        print(cnt)
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            delete from emp where e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        
        return cnt
    
    def update(self, e_id,e_name,gen,addr):
        sql = f"""
            update emp set
            e_name = '{e_name}',
            gen = '{gen}',
            addr = '{addr}'
            where e_id = '{e_id}'
        """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
                
        return cnt

    def __del__(self):
        self.cur.close()    
        self.con.close()

if __name__== '__main__':
    de = DaoEmp()
    # emp1 = de.selectList()
    # emp2 = de.selectOne('4')
    # cnt = de.insert('4','4','4','4')
    # cnt = de.update('4', '5', '5', '5')
    # cnt = de.delete('4')
    # print(cnt)

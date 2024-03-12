import sqlite3

class DaoExam:
    def __init__(self):
        self.con = sqlite3.connect('exam.db')
        self.cur = self.con.cursor()
    
    def selectList(self):
        sql = """
            select * 
            from exam 
            order by e_id desc;
        """
        self.cur.execute(sql)
        list = self.cur.fetchall()
        ret = []
        for e in list:
            ret.append({'e_id':e[0],'e_que':e[1],'ans1':e[2],'ans2':e[3],'ans3':e[4],'ans4':e[5],'ans':e[6]})
            
        return ret
    def selectOne(self, e_id):
        sql = f"""
            select * 
            from exam 
            where e_id = '{e_id}' 
            order by e_id
        """
        self.cur.execute(sql)
        e = self.cur.fetchone()
        vo = {'e_id':e[0],'e_que':e[1],'ans1':e[2],'ans2':e[3],'ans3':e[4],'ans4':e[5],'ans':e[6]}
            
        return vo
    
    def insert(self, e_id,e_que,ans1,ans2,ans3,ans4,ans):
        sql = f"""
            insert into exam(e_id,e_que,ans1,ans2,ans3,ans4,ans)
            values('{e_id}','{e_que}','{ans1}','{ans2}','{ans3}','{ans4}','{ans}')
        """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        
        return cnt
    
    def delete(self, e_id):
        sql = f"""
            delete from exam where e_id = '{e_id}'
        """
        
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
        
        return cnt
    
    def update(self, e_id,e_que,ans1,ans2,ans3,ans4,ans):
        sql = f"""
            update exam set
            e_que = '{e_que}',
            ans1 = '{ans1}',
            ans2 = '{ans2}',
            ans3 = '{ans3}',
            ans4 = '{ans4}',
            ans = '{ans}'
            where e_id = '{e_id}'
        """
        self.cur.execute(sql)
        cnt = self.cur.rowcount
        self.con.commit()
                
        return cnt 
      
    def __del__(self):
        self.cur.close()
        self.con.close()

if __name__ == '__main__':
    de = DaoExam()
    exam1 = de.selectList()
    exam2 = de.selectOne(1)
    #exam3 = de.insert(4, 4, 4, 4, 4, 4, 4)
    #exam4 = de.update(4, 5, 5, 5, 5, 5, 5)
    #exam5 = de.delete(4)
    print(exam1)
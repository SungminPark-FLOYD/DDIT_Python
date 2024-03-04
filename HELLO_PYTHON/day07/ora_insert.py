import cx_Oracle

#방법 1-----------------------------
# # 오라클 접속       
# conn = cx_Oracle.connect('python/py@localhost:1521/xe')
# cs = conn.cursor()
#
# # sql 구문 실행
# sql =   "insert into emp values('3','3','3','3')"
# cs.execute(sql)
# conn.commit()
#
# cs.close()    
# conn.close()

#방법 2 --------------------------------------------------------
# import cx_Oracle

conn = cx_Oracle.connect('python/py@localhost:1521/xe')
cs = conn.cursor()

e_id = 4
e_name = 4
gen = 4
addr = 4

# format String 적용하기
sql = f"""
        insert into emp
            (e_id, e_name, gen, addr) 
        values
            ('{e_id}','{e_name}','{gen}','{addr}')
    """
cs.execute(sql)   
# 적용되는 행 받아오기
print(cs.rowcount)

cs.close()
#commit 필수
conn.commit()
conn.close()
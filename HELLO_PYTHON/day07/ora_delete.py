import cx_Oracle

conn = cx_Oracle.connect('python/py@localhost:1521/xe')
cs = conn.cursor()

e_id = 4

# format String 적용하기
sql = f"""
       delete from EMP where e_id = '{e_id}'        
    """
cs.execute(sql)   
# 적용되는 행 받아오기
print(cs.rowcount)

#commit 필수
conn.commit()

cs.close()
conn.close()
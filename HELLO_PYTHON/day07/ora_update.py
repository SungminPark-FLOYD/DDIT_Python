import cx_Oracle

conn = cx_Oracle.connect('python/py@localhost:1521/xe')
cs = conn.cursor()

e_id = 4
e_name = 6
gen = 6
addr = 6

# format String 적용하기
sql = f"""
        update emp set
            e_name = '{e_name}',
            gen = '{gen}',
            addr = '{addr}'
    
        where e_id = '{e_id}'
        
    """
cs.execute(sql)   
# 적용되는 행 받아오기
print(cs.rowcount)

cs.close()
#commit 필수
conn.commit()
conn.close()
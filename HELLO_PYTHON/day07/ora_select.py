import cx_Oracle

# 오라클 접속       
conn = cx_Oracle.connect('python/py@localhost:1521/xe')
cs = conn.cursor()

# sql 구문 실행
sql =   "select * from emp"
rs = cs.execute(sql)

# lst = list(rs)
# print(lst)
#
# for r in rs:
#     print(r)

rows = cs.fetchall()
print(rows)
    
cs.close()    
conn.close()


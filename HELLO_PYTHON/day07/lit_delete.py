import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()

col1 = 3
# format String 적용하기
sql = f"""
        DELETE FROM sample
        where col01 = '{col1}'
    """
cursor.execute(sql)   
# 적용되는 행 받아오기
print(cursor.rowcount)

cursor.close()
#commit 필수
con.commit()
con.close()
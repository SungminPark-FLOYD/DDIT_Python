import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()

col1 = 3
col2 = 3
col3 = 3

# format String 적용하기
sql = f"""
        insert into sample
            (col01, col02, col03) 
        values
            ('{col1}','{col2}','{col3}')
    """
cursor.execute(sql)   
# 적용되는 행 받아오기
print(cursor.rowcount)

cursor.close()
#commit 필수
con.commit()
con.close()
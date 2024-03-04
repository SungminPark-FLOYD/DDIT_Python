import sqlite3

con = sqlite3.connect('sample.db')
cursor = con.cursor()

col1 = 3
col2 = 6
col3 = 6

# format String 적용하기
sql = f"""
        update sample SET
            col02 = '{col2}',
            col03 = '{col3}'
        where col01 = '{col1}'
    """
cursor.execute(sql)   
# 적용되는 행 받아오기
print(cursor.rowcount)

cursor.close()
#commit 필수
con.commit()
con.close()
import sqlite3
 
con = sqlite3.connect('sample.db')
cursor = con.cursor()

cursor.execute('SELECT * FROM sample;')
sample = cursor.fetchall()

print(sample)

con.close()
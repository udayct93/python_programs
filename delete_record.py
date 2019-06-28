import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="rocky@1234", host="127.0.0.1", port="5432")
print("Database Connected....")
cur=conn.cursor()
cur.execute("delete from person where pid=3")
cur.execute("select pid,name,age,address from person")
rows=cur.fetchall()
for row in rows:
   print("pid=",row[0])
   print("name=",row[1])
   print("age=", row[2])
   print("address=", row[3])
conn.close()
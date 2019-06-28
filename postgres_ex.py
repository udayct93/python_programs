import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="rocky@1234", host="127.0.0.1", port="5432")
print("Database Connected....")
cur=conn.cursor()
cur.execute("insert into person(pid,name,age,address)values(01,'vinay',27,'bangalore')")
cur.execute("insert into person(pid,name,age,address)values(02,'akash',25,'mangalore')")
cur.execute("insert into person(pid,name,age,address)values(03,'anirud',26,'mysore')")
cur.execute("insert into person(pid,name,age,address)values(04,'anand',25,'dharwad')")
cur.execute("insert into person(pid,name,age,address)values(05,'rakshit',29,'udapi')")
print("inserted successfully")
conn.commit()
conn.close()

import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="rocky@1234", host="127.0.0.1", port="5432")
cur = conn.cursor()
cur.execute("select pid,name,age,address from person")
rows=cur.fetchall()
for row in rows:
   print("pid=",row[0])
   print("name=",row[1])
   print("age=", row[2])
   print("address=", row[3])
conn.close()
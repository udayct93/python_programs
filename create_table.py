import psycopg2
conn = psycopg2.connect(database="postgres", user="postgres", password="rocky@1234", host="127.0.0.1", port="5432")
print("Database Connected....")
cur=conn.cursor()
cur.execute("create table pers(pid int primary key not null,name text not null,age int not null,address char(50) not null);")
print('table created successfully')
conn.commit()
conn.close()


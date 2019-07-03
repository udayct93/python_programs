import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer,update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:rocky@1234@localhost:5432')
base = declarative_base()
Session = sessionmaker(engine)
session = Session()
class customer(base):
    __tablename__ ='customers'
    cid = Column(Integer, primary_key=True)
    cname = Column(String)
    city = Column(String)

base.metadata.create_all(engine)
print("Table Successfully created!")

cstmrs=([customer( cname="manoj", city="bangalore"),
        customer(cname="akash", city="mangalore"),
        customer( cname="aditya", city="badami")])
a = session.query(customer)
# session.add_all(cstmrs)
session.commit()
print("Values Inserted to Tables Successfully")
# for y in a.all():
#     print(y.cid,y.cname,y.city)
#     session.query(customer).filter(customer.cid == 3).update({customer.cname: "anand", })
# session.commit()
session.query(customer).filter(
    customer.cname.ilike("m%")
).delete(synchronize_session='fetch')
session.commit()
for y in a.all():
    print(y.cid,y.cname,y.city)


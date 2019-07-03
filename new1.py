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
class product(base):
    __tablename__ ='products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(Integer)
    # address=Column(varchar(20))
base.metadata.create_all(engine)
print("Table Successfully created!")

a =[product( id=1,name="mobile", size=70),
      product( id=2,name="mouse", size=80),
      product(id=3, name="keyboard", size=90)]
a = session.query(product)



#
print("Values Inserted to Tables Successfully")
session.commit()
session.query(product).filter(product.id==3).update({product.name:"anand",})

#
# stmt=update(product).where(product.c.id==3).values(name="laptop")
# for x in a.all():
#     print(x.id,x.name,x.size)

# session.query(product).filter(
#     product.name.ilike("W%")
# ).update({"quantity": 60}, synchronize_session='fetch')
# session.commit()
# b=session.query(product)
# for x in b.all():
#     print(x.id,x.name,x.size)

# print("Values updated to Tables Successfully")
# session.commit()
# x = session.query(product).get(2)
# print ("id: ", x.id,"Name: ", x.name,"size:", x.size)
# x=x.name='AJAY'''
# session.commit()

# i =product.filter(product.name == 'anand')
# session.delete(i)
# session.commit()
# for x in a.all():
#     print(x.id,x.name,x.size)
# session.query(product).filter(
#     product.name.ilike("%l")
# ).delete(synchronize_session='fetch')
session.commit()
for x in a.all():
    print(x.id,x.name,x.size)

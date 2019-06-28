import sqlalchemy
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:rocky@1234@localhost:5432')
base = declarative_base()
class product(base):
    __tablename__ ='products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(Integer)
Session = sessionmaker(engine)
session = Session()
base.metadata.create_all(engine)
print("Table Successfully created!")

'''item=[product( id=4,name="books", size=70),
      product( id=5,name="bag", size=80),
      product(id=6, name="pencil", size=90)]'''
a = session.query(product)

for x in a.all():
    print(x.id,x.name,x.size)

print("Values Inserted to Tables Successfully")

session.commit()

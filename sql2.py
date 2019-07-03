from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Creates a engine
engine = create_engine('postgresql://postgres:rocky@1234@localhost')
# creates base class
base = declarative_base()

# creating Model  with columns
class Organization(base):
    __tablename__ = 'organization'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    size = Column(Integer)

# Creating Session
Session = sessionmaker(engine)
session = Session()

# Creating Table Structure
base.metadata.create_all(engine)
print("Table Successfully created!")

# Inserting values
coextrix = [Organization( name="Coextrix Technologies Pvt Ltd.", size=70),
            Organization( name="Cargill Technologies Pvt Ltd.", size=300000)]


# Retriving the all the values
a = session.query(Organization)

# Iterating values for printing
for x in a.all():
    print(x.name,x.size)

print("Values Inserted to Tables Successfully")
session.add_all(coextrix)

# commit to the table
session.commit()

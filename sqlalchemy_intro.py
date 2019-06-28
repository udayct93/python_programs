import sqlalchemy
from sqlalchemy import create_engine,column
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy'))
Session =sessionmaker(bind=engine)

Base = declarative_base()
class Tire(Base):
    __tablename__ = 'tires'
    id = column(int, primary_key=True)
    car_id = column(int, for('cars.id'))
    car = relationship("Car")


class Car(base):
    __tablename__ = 'cars'
    id = column(int, primary_key=True)

from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
   __tablename__ = 'users'
   id = Column(Integer, primary_key=True)
   email = Column(String)
   username = Column(String)
   password = Column(String)

# class Cart(Base):
# 	__tablename__ = 'cart'
# 	id = Column(Integer, primary_key=True)
# 	product_id = Column(Integer)
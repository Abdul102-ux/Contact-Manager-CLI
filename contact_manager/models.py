from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    contacts = relationship('Contact', back_populates='user')

class Contact(Base):
    __tablename__ = 'contacts'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))          
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='contacts')
    group = relationship('Group', back_populates='contacts')  

class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    contacts = relationship('Contact', back_populates='group')

import sys
import os

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	email = Column(String(80), nullable = False)
	picture = Column(String(80))


class Developer(Base):
	__tablename__ = 'developer'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	image = Column(String(80))
	u_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)


class Game(Base):
	__tablename__ = 'game'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	image = Column(String(80))
	d_id = Column(Integer, ForeignKey('developer.id'))
	developer = relationship(Developer)
	u_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User)


engine = create_engine('sqlite:///gamecatalog.db')

Base.metadata.create_all(engine)
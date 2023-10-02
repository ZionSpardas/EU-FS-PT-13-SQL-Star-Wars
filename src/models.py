import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Users(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    
    name = Column(String(250), nullable=False)
    password = Column(Integer, nullable=False)


class Planets(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    planet_id = Column(Integer, primary_key=True)
   
    name = Column(String(250))
    diameter = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))


class Characters(Base):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    character_id = Column(Integer, primary_key=True)
   
    name = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    eye_color = Column(String(250))

class FavoritePlanet(Base):
    __tablename__ = 'favoriteplanet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favplanet_id = Column(Integer, ForeignKey('planet.id'))
    planet_id = relationship(Planets)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    
class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    favcharacter_id = Column(Integer, ForeignKey('character.id'))
    character_id = relationship(Characters)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(Users)
    



# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(20), nullable=False)
    edad = Column(Integer)
    correo = Column(String(80), unique=True, nullable=False)
    foto_perfil = Column(String(250))

# Personajes 
class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)
    raza = Column(String(250), nullable=False)
    foto = Column(String(250), nullable=True)

# Naves 
class Naves(Base):
    __tablename__ = 'naves'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250),nullable=False)
    tipodenave = Column(String(250), nullable=True)
    fecha_fabricacion = Column(String(250), nullable=False)
    foto = Column(String(250), nullable=True)

# Batallas 
class Batalla(Base):
    __tablename__ = 'batalla'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250),nullable=False)
    vencedor = Column(String(250), nullable=True)
    aliados = Column(String(250), nullable=False)
    enemigos = Column(String(250), nullable=False)
    foto = Column(String(250), nullable=True)

# Armas 
class Armas(Base):
    __tablename__ = 'armas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250),nullable=False)
    fabricante = Column(String(250), nullable=True)
    material = Column(String(250), nullable=False)
    tipo_arma = Column(String(250), nullable=False)
    foto = Column(String(250), nullable=True)

# Planetas 
class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250),nullable=False)
    latitud = Column(String(250), nullable=False)
    longitud = Column(String(250), nullable=False)
    tipo_planeta = Column(String(250), nullable=False)
    foto = Column(String(250), nullable=True)

# Favoritos
class Personaje_Favorito(Base):
    __tablename__ = 'personaje_favorito'
    id_fav_personaje = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_personaje = Column(Integer, ForeignKey('personaje.id'), nullable=False)

class Naves_Favorito(Base):
    __tablename__ = 'naves_favorito'
    id_fav_personaje = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_naves = Column(Integer, ForeignKey('naves.id'), nullable=False)

class Planeta_Favorito(Base):
    __tablename__ = 'planeta_favorito'
    id_fav_personaje = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_planeta = Column(Integer, ForeignKey('planeta.id'), nullable=False)

class Batalla_Favorito(Base):
    __tablename__ = 'batalla_favorito'
    id_fav_personaje = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_batalla = Column(Integer, ForeignKey('batalla.id'), nullable=False)

class Armas_Favorito(Base):
    __tablename__ = 'armas_favorito'
    id_fav_personaje = Column(Integer, primary_key=True)
    id_usuario = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    id_armas = Column(Integer, ForeignKey('armas.id'), nullable=False)
    
    
    
    

 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

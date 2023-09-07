from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from typing import Union

from  model import Base


class Valve(Base):
    __tablename__ = 'valve'

    id = Column("pk_valve", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    descricao = Column(String(200))
    tipo = Column(String(140))
    vazao = Column(Float)



    def __init__(self, nome:str, descricao:str, tipo:str, vazao:float):
        
        self.nome = nome
        self.descricao = descricao
        self.vazao = vazao
        self.tipo = tipo



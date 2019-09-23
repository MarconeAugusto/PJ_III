from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from entidades.base import Base

class TipoEvento(object):
    SAIU_AUT_OK = 1
    SAIU_AUT_NOK = 2
    ESTACIONOU_AUT_OK = 3
    ESTACIONOU_AUT_NOK = 4

    evento_str = {
        SAIU_AUT_OK: 'Saiu AUT OK',
        SAIU_AUT_NOK: 'Saiu AUT NOK',
        ESTACIONOU_AUT_OK: 'Estacionou AUT OK',
        ESTACIONOU_AUT_NOK: 'Estacionou AUT NOK'
    }

    lista_estados = [
        SAIU_AUT_OK, SAIU_AUT_NOK,
        ESTACIONOU_AUT_OK, ESTACIONOU_AUT_NOK
    ]

class Evento(Base):
    '''
    Relacao one to many com vaga
    '''
    __tablename__ = 'evento'

    id = Column(Integer, primary_key=True)
    tipo = Column(Integer)
    data = Column(DateTime)
    vaga_id = Column(Integer, ForeignKey('vaga.id'), nullable=False)
    # vaga_id = Column(Integer, ForeignKey('vaga.id'), primary_key=True)

    def __init__(self, tipo, vaga_id, data=None):
        self.tipo = tipo
        self.vaga_id = vaga_id
        self.data = data if data is not None else datetime.now()


    def converteParaJson(self):
        eventoJson = {
            'id': self.id,
            'tipo': TipoEvento.evento_str[self.tipo],
            'data': self.data
        }
        return eventoJson
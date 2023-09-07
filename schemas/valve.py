from pydantic import BaseModel
from typing import Optional, List
from model.valve import Valve


class ValveSchema(BaseModel):
    """Define como uma nova válvula a ser inserida deve ser representada"""
    nome: str = "RETQ408BV"
    descricao: str = "Válvula de Bloqueio"
    tipo: str = "Gaveta"
    vazao: float = 15200


class ValveBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no nome da válvula."""
    nome: str = "Válvula XXX"


class ValveBuscaIdSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca. Que será
    feita apenas com base no ID da válvula."""
    id: int = 1


class ListagemValveSchema(BaseModel):
    """Define como uma listagem de válvulas será retornada."""
    valve: List[ValveSchema]


def apresenta_valves(valves: List[Valve]):
    """Retorna uma representação da válvula seguindo o schema definido em
    ValveViewSchema."""
    result = []
    for valve in valves:
        result.append({
            "nome": valve.nome,
            "descricao": valve.descricao,
            "tipo": valve.tipo,
            "vazao": valve.vazao,
        })

    return {"valves": result}


class ValveViewSchema(BaseModel):
    """Define como uma válvula será retornado: válvula ."""
    id: int = 1
    nome: str = "RETQ408BV"
    descricao: str = "Válvula de Bloqueio"
    tipo: str = "Gaveta"
    vazao: float = 15200


class ValveDelSchema(BaseModel):
    """Define como deve ser a estrutura do dado retornado após uma requisição
    de remoção."""
    mesage: str
    nome: str


class ValveUpdateSchema(BaseModel):
    id: int
    nome: str
    descricao: str
    tipo: str
    vazao: float

def apresenta_valve(valve: Valve):
    """Retorna uma representação da válvula seguindo o schema definido em
    ValveViewSchema."""
    return {
        "id": valve.id,
        "nome": valve.nome,
        "descricao": valve.descricao,
        "tipo": valve.tipo,
        "vazao": valve.vazao
    }

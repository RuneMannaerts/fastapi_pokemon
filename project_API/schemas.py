from typing import List
import datetime as _dt
import pydantic as _pydantic

#pokemon database

class _PokemonBase(_pydantic.BaseModel):
    pokedex: int
    pokename: str
    type1: str
    region: int


class PokemonCreate(_PokemonBase):
    pokedex: int
    pokename: str
    type1: str
    region:int


class Pokemon(_PokemonBase):
    id: int

    class Config:
        orm_mode = True

#region database 

class _RegionBase(_pydantic.BaseModel):
    name: str


class RegionCreate(_RegionBase):
    name: str

class Region(_RegionBase):
    id: int

    class Config:
        orm_mode = True

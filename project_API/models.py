import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm

import database as _database

class Pokemon(_database.Base):
    __tablename__ = "pokemons"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    pokedex = _sql.Column(_sql.Integer, unique=True, index=True)
    pokename = _sql.Column(_sql.String)
    type1 = _sql.Column(_sql.String) #foreign key possible for further meshing of database and scaling
    region=_sql.Column(_sql.Integer, _sql.ForeignKey("regions.id"))
    
class Region(_database.Base):
    __tablename__ = "regions"
    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    name = _sql.Column(_sql.Integer, unique=True, index=True)
    
        
import sqlalchemy.orm as _orm

import models as _models, schemas as _schemas, database as _database


def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine)


def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# user table starts here
""" 
def get_users(db: _orm.Session, skip: int = 0, limit: int = 100):
    return db.query(_models.User).offset(skip).limit(limit).all()

 """
# pokemon table starts here
""" 
def get_pokemon_by_pokedex(db: _orm.Session, pokedex: int):
    return db.query(_models.Pokemon).filter(_models.Pokemon.pokedex == pokedex).first()

"""

#pokemon

def get_pokemon(db: _orm.Session, pokemon_id: int):
    return db.query(_models.Pokemon).filter(_models.Pokemon.id == pokemon_id).first()

def create_pokemon(db: _orm.Session, pokemon: _schemas.PokemonCreate):
    db_pokemon = _models.Pokemon(pokedex=pokemon.pokedex, pokename=pokemon.pokename, type1=pokemon.type1, region=pokemon.region)
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def delete_pokemon(db: _orm.Session, pokemon_id: int):
    db.query(_models.Pokemon).filter(_models.Pokemon.id == pokemon_id).delete()
    db.commit()

#region

def get_region(db: _orm.Session, region_id: int):
    return db.query(_models.Region).filter(_models.Region.id == region_id).first()

def create_region(db: _orm.Session, region: _schemas.RegionCreate):
    db_region = _models.Region(name=region.name)
    db.add(db_region)
    db.commit()
    db.refresh(db_region)
    return db_region

def delete_region(db: _orm.Session, region_id: int):
    db.query(_models.Region).filter(_models.Region.id == region_id).delete()
    db.commit()

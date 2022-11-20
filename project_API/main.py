from typing import List
import fastapi as _fastapi
from fastapi.middleware.cors import CORSMiddleware
import sqlalchemy.orm as _orm
import services as _services, schemas as _schemas

app = _fastapi.FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "https://front-end-api-rune-pokemon.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


_services.create_database()


"""

@app.get("/users/", response_model=List[_schemas.User])
def read_users(
    skip: int = 0,
    limit: int = 10,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    users = _services.get_users(db=db, skip=skip, limit=limit)
    return users

"""

#pokemon
 
@app.get("/pokemons/{pokemon_id}", response_model=_schemas.Pokemon)
def read_pokemon(pokemon_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_pokemon = _services.get_pokemon(db=db, pokemon_id=pokemon_id)
    if db_pokemon is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this pokemon does not exist"
        )
    return db_pokemon


@app.post("/pokemons/", response_model=_schemas.Pokemon)
def create_pokemon(
    pokemon: _schemas.PokemonCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):    
    return _services.create_pokemon(db=db, pokemon=pokemon)

@app.delete("/pokemons/{pokemon_id}")
def delete_pokemon(pokemon_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_pokemon(db=db, pokemon_id=pokemon_id)
    return {"message": f"successfully deleted post with id: {pokemon_id}"}

#region

@app.get("/regions/{region_id}", response_model=_schemas.Region)
def read_region(region_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    db_region = _services.get_region(db=db, region_id=region_id)
    if db_region is None:
        raise _fastapi.HTTPException(
            status_code=404, detail="sorry this region does not exist"
        )
    return db_region

@app.post("/regions/", response_model=_schemas.Region)
def create_region(
    region: _schemas.RegionCreate, db: _orm.Session = _fastapi.Depends(_services.get_db)
):    
    return _services.create_region(db=db, region=region)

@app.delete("/regions/{region_id}")
def delete_region(region_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)):
    _services.delete_region(db=db, region_id=region_id)
    return {"message": f"successfully deleted post with id: {region_id}"}

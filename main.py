from fastapi import FastAPI, HTTPException
from typing import List, Optional
from city_data import states, states_cities

app = FastAPI(
    title="API de Estados do Brasil",
    description="Uma API para listar os estados do Brasil.",
    version="1.0.0",
)

@app.get("/states/", response_model=List[dict])
async def get_states():
    return states

@app.get("/states/{state_id}", response_model=dict)
async def get_state_by_id(state_id: int):
    for state in states:
        if state["id"] == state_id:
            return state
    raise HTTPException(status_code=404, detail="State not found")

@app.get("/states/{state_id}/cities", response_model=List[dict])
async def get_cities_by_state(state_id: int):
    if state_id in states_cities:
        return states_cities[state_id]
    raise HTTPException(status_code=404, detail="State not found")

@app.get("/cities/{city_id}", response_model=dict)
async def get_city_by_id(city_id: int):
    for cities in states_cities.values():
        for city in cities:
            if city["id"] == city_id:
                return city
    raise HTTPException(status_code=404, detail="City not found")
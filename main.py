from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date

app = FastAPI(
    title="API de Gestión de Tareas",
    description="API para gestionar una lista de tareas (To-Do List)",
    version="1.0.1"
)

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str
    vencimiento: date
    estado: bool 

tareas = [
    {
        "id": 1,
        "titulo": "Estudiar para el examen",
        "descripcion": "Repasar los apuntes de TAI",
        "vencimiento": "2024-02-14",
        "estado": True
    }
]


@app.get("/", tags=["Inicio"])
def main():
    return {'Hello World from FastAPI': 'API de Gestión de Tareas'}

@app.get("/tareas", tags=["Tareas"])
def obtener_todas_las_tareas():
    return {"tareas": tareas}

@app.get("/tareas/{id}", tags=["Tareas"])
def obtener_tarea_por_id(id: int):
    for tarea in tareas:
        if tarea["id"] == id:
            return {"tarea": tarea}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


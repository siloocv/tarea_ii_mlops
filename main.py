from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

from starlette import status

api = FastAPI(
    title="MLOps second API",
    description="MLOps second API",
    version="0.0.1",
)

users_db = []

@api.post("/users", tags=["Users"])
async def user_registration(data: dict):
    if "name" not in data or "email" not in data or "username" not in data:
        raise HTTPException(status_code=400, detail="Faltan campos requeridos")

    user_id = str(uuid.uuid4())
    user_data = {
        "id": user_id,
        "name": data["name"],
        "email": data["email"],
        "username": data["username"]
    }
    users_db.append(user_data)

    return {
        "response": f"Se ha creado exitosamente el usuario {data['username']} con el email {data['email']}",
        "id": user_id,
        "name": data["name"],
        "status_code": 201
    }

@api.get("/users/{username}", tags=["Users"])
async def get_user(username: str):
    for user in users_db:
        if user["username"] == username:
            return user
    return {"error": "Usuario no encontrado"}

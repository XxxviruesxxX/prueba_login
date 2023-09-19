from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import crud
import schemas
import database

app = FastAPI()

# Configura el middleware CORS
origins = [
    "http://localhost",
    "http://192.168.105.92:8081",
    "http://localhost:8081",
    "http://127.0.0.1:8000"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta para el registro de usuario
@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)

# Ruta de ejemplo para el inicio de sesión
@app.post("/login")
async def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    print("entra login")
    db_user = crud.get_user_by_username(db, user.username)
    if not db_user:
        raise HTTPException(status_code=400, detail="Usuario no encontrado")
    if not crud.verify_password(user.password, db_user.password_hash):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    return {"message": "Inicio de sesión exitoso"}

# Ruta de ejemplo sin relación con el usuario
@app.post("/login2")
def post_login():
    print("entra post")
    return "Respuesta login"

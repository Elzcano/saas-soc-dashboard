from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.models.user import User
from app.database import SessionLocal
from sqlalchemy.orm import Session

# Mismos valores que en auth.py
SECRET_KEY = "clave_secreta_super_segura"
ALGORITHM = "HS256"

# Esta dependencia extrae el token del encabezado Authorization: Bearer <token>
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Reutilizamos conexión a base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función para obtener el usuario actual a partir del token JWT
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token inválido o expirado",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Decodificar el token usando la clave secreta
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")  # sub = subject (usuario)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    # Buscar el usuario en la base de datos
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception

    return user

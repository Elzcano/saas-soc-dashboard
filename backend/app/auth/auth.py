from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

# ⚠️ Esta clave debe mantenerse en secreto en producción (puedes moverla a variables de entorno)
SECRET_KEY = "clave_secreta_super_segura"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuración para hashear contraseñas usando bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Verificar que la contraseña ingresada coincida con la contraseña hasheada
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Generar un hash seguro de la contraseña (para guardar en la BD)
def get_password_hash(password):
    return pwd_context.hash(password)

# Crear el JWT token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

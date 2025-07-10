from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de la base de datos SQLite local
DATABASE_URL = "sqlite:///./test.db"

# Crear motor de conexión
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Crear sesión para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base de la cual heredarán todos los modelos
Base = declarative_base()

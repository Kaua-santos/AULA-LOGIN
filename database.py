# pip install sqlalchemy alembic fastapi uvicorn jinja2 python_multipart python-dotenv
from sqlalchemy import Column,Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os 
Base = declarative_base()

# tabela no banco de dados 
class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(100), nullable=False)

# carrear as variaveis de ambiete
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine, autoflush=False)

# função para conectar com o banco
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()





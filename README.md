# configurar o alembic

no terminal: python -m alembic init migrations

Agora edite o arquivo alembic.init

linha 89 
apague o link e deixe assim:
sqlalchemy.url = 

# para rodar o alembic 

# gerar a migration
python -m alembic revision --autogenerate -m "criar tabela usuarios"

#Aplicar a migration no banco 
python -m alembic upgrade head
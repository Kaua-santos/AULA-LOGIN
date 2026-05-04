from fastapi import FastAPI, Depends, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import get_db, Usuario

# Rodar o codigo 
# python -m uvicorn main:app --reload

app = FastAPI(title="Sistema de loguin")

templates = Jinja2Templates(directory="templates")

# sistema SSR
# Rotas (GET, POST)
@app.get("/cadastro")
def tela_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastro.html",
        {"request": request}
    )

@app.get("/login")
def tela_login(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request}
    )

# rota para cadastrar 
@app.post("/cadastro")
def cadastrar_usuario(
    request: Request,
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
):
    user_existente = db.query(Usuario).filter_by(email==email).first()

    if user_existente: 
        return templates.TemplateResponse(
            request,
            "cadastro.html",
            {"request": request, "erro": "Email ja cadastrado"}
        )
    
    novo_usuario = Usuario(email=email, senha=senha)
    db.add(novo_usuario)
    db.commit()

    return RedirectResponse(url="/login", status_code=303)


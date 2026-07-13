from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

banco_de_dados = []


class Usuario(BaseModel):
    nome: str
    email: str
    cargo: str


@app.get("/usuarios")
def listar_usuarios():
    return {"usuarios cadastrados": banco_de_dados}


@app.post("/usuarios")
def cadastrar_usuario(novo_usuario: Usuario):
    banco_de_dados.append(novo_usuario.dict())
    return {
        "mensagem": "Usuário cadastrado com sucesso!",
        "dados_salvos": novo_usuario.dict(),
    }

@app.delete("/usuarios/{email}")
def remover_usuario(email: str):

    for usuario in banco_de_dados:

     
        if usuario["email"] == email:
            banco_de_dados.remove(usuario)  # Remove da lista
            return {"mensagem": f"Usuário com e-mail {email} removido com sucesso!"}

    return {"erro": "Usuário não encontrado."}

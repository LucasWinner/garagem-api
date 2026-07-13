from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

banco_de_dados = []


class Veiculo(BaseModel):
    modelo: str
    cilindradas: int
    cor: str


@app.post("/veiculos")
def cadastrar_veiculo(novo_veiculo: Veiculo):
    if novo_veiculo.cilindradas <= 0:
        return {"erro": "cilindradas deve ser maior que zero."}
    else:
        banco_de_dados.append(novo_veiculo.dict())
        return {
            "mensagem": "Veiculo cadastrado com sucesso!",
            "dados salvos": novo_veiculo.dict(),
        }


@app.put("/veiculos/{modelo}")
def atualizar_veiculo(modelo: str, veiculo_atualizado: Veiculo):

    # 1. Variável minúscula para não confundir com a Classe Pydantic
    for veiculo_atual in banco_de_dados:

        # 2. Comparamos o banco com o 'modelo' que veio na URL!
        if veiculo_atual["modelo"] == modelo:
            # Se achou, atualiza os dados e encerra a função com o return
            veiculo_atual.update(veiculo_atualizado.dict())
            return {"mensagem": f"Veículo {modelo} atualizado com sucesso!"}

    # 3. O ERRO FICA FORA DO FOR!
    # O código só chega nesta linha se rodou a lista toda e não achou.
    return {"erro": "Veiculo não encontrado."}


@app.get("/veiculos")
def listar_veiculos():
    return {"Veiculos cadastrados": banco_de_dados}

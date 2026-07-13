# API de Gestão de Garagem (Veículos) 🚗🏍️

Uma API RESTful desenvolvida em Python para gestão e registo de veículos, construída com foco em boas práticas de engenharia de software, validação estrita de dados e conteinerização.

## 🚀 Tecnologias Utilizadas
* **Python** (Linguagem base)
* **FastAPI** (Framework web de alta performance)
* **Pydantic** (Validação rigorosa de regras de negócio e tipagem)
* **Docker & Docker Compose** (Orquestração e isolamento do ambiente)

## ⚙️ Funcionalidades (CRUD)
* `POST /veiculos`: Registo de novos veículos com validação de regras de negócio (ex: bloqueio de cilindradas nulas ou negativas).
* `GET /veiculos`: Listagem dos veículos guardados.
* `PUT /veiculos/{modelo}`: Atualização de dados de um veículo existente na base.

## 🛠️ Como executar o projeto
Certifique-se de que tem o Docker instalado na sua máquina. No terminal, navegue até à pasta do projeto e execute o comando:

```bash
docker compose up --build

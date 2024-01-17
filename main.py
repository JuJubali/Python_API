from fastapi import FastAPI

myApp = FastAPI() # criar API

""" Troca de dados. Enviar e REceber
Get -> Pegar dados da API
json {} """

vendas = {
    1: {"item": camisa, "preco": 25.50, "unidade": 3}, 
    2: {"item": pelicula, "preco": 7.10, "unidade": 2},
    3: {"item": bolsa, "preco": 77.40, "unidade": 1},
    
}

# Caminhos acesasdo - O que acontece
""" Decorator -> Linha que atribui uma função a próxima linha 
Sempre antes da função"""
@myApp.get("/") # Decorator 
def home():
    return "Um site"
    return {"vendas": len(vendas)}

@myApp.get("/vendas/{id_vendas}") # {variáveis}
def pegar_venda(id_vendas: int):
    if id_vendas in vendas:
        return vendas[id_vendas]
    else:
        return {"Erro": "Venda Indisponível"}

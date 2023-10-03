from flask import Blueprint, jsonify, make_response, request
from bd import products, insert_product
from datetime import date

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return {
        "greeting": ["hello", "world"],
        "date": date.today()
    }
    
@main.route('/products', methods=['GET'])
def productsList():
    dados = products()
    print(dados)
    minhalista = []
    for x in dados:
        minhalista.append(
            {
                'id': x[0],
                'name': x[1],
                'price': x[2]
            }
        )  
    return make_response(
        jsonify(
            mensagem='Lista de produtos',
            dados=minhalista
        ),
        200
    )

@main.route('/products', methods=['POST'])
def create_products():
    product = request.json
    insert_product(product)
    return make_response(
        jsonify(
            mensagem='Produto cadastrado com sucesso.',
            dados=product
        ),
        200
    )
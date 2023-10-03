
#desenvolvimento
from flask import Flask, request, jsonify, make_response
from bd import products
from bd import insert_product
#@app.route('/products', methods=['GET'])
def productsList_p():
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
    
#@app.route('/products', methods=['POST'])
def create_products_p():
    product = request.json
    insert_product(product)
    return make_response(
        jsonify(
            mensagem='Produto cadastrado com sucesso.',
            dados=product
        ),
        200
    )
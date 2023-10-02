
import os
from flask import Flask, jsonify, make_response, request


from routes import main
app = Flask(__name__)

class MeuProduto:
    def __init__(self,name, price):
        self.name = name,
        self.price = price

#producao
#def server_app():
#    app.register_blueprint(main)
#    print('Rodando')
#       
#    return app

#desenvolvimento
from bd import products
from bd import insert_product
@app.route('/products', methods=['GET'])
def productsList():
    #return jsonify([
    #    {'id':1,'name':'silva'},
    #    {'id':3,'name':'yan'},
    #])
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
    
@app.route('/products', methods=['POST'])
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

app.run()


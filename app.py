
import os
from flask import Flask, jsonify

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
import json
@app.route('/products', methods=['GET'])
def productsList():
    #return jsonify([
    #    {'id':1,'name':'silva'},
    #    {'id':3,'name':'yan'},
    #])
    dados = products()
    minhalista = []
    #for x in dados:
    #   minhalista.append(MeuProduto(x[1],x[2]))
          
    return jsonify(dados)
    
app.run()


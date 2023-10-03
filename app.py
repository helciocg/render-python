
import os
from flask import Flask, request #producao: jsonify, make_response, 

#https://www.youtube.com/watch?v=qg3BNCa_NdQ

from routes import main
app = Flask(__name__)

class MeuProduto:
    def __init__(self,name, price):
        self.name = name,
        self.price = price

#producao
def server_app():
    app.register_blueprint(main)
    print('Rodando')
       
    return app

app.run()



import os
from flask import Flask, jsonify

from routes import main
app = Flask(__name__)

def server_app():
    app.register_blueprint(main)
    print('Rodando')
       
    return app
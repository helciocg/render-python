from flask import Blueprint,jsonify

from bd import products
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
    return jsonify(
            products()
    )
import pymysql
import os
from dotenv import load_dotenv
from mysql.connector import Error
import mysql.connector

load_dotenv("config.env")

connection = mysql.connector.connect(
    host= os.getenv("DB_HOST"),
    user=os.getenv("DB_USERNAME"),
    passwd= os.getenv("DB_PASSWORD"),
    db= os.getenv("DB_NAME"),
    autocommit = True,
    ssl_ca="/etc/ssl/certs/ca-certificates.crt"
)
def products():
    dados = []
    mycursor = connection.cursor(pymysql.cursors.DictCursor)
    mycursor.execute("SELECT * FROM products;")
    dados = mycursor.fetchall()
    return dados


def insert_product(product):
    mycursor = connection.cursor(pymysql.cursors.DictCursor)
    sql = f"INSERT INTO products(id, name, price) VALUES({product['id']},'{product['name']}',{product['price']});"
    print(sql)
    mycursor.execute(sql)
    connection.commit()
    return product

if __name__ == '__main__':
    mylist = products()
    for x in mylist:
        print(x)  
    #print("{:.2f}, {} ".format(
    # x[2], x[1]))
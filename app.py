from flask import Flask 

#https://www.youtube.com/watch?v=qg3BNCa_NdQ

from routes import main
app = Flask(__name__)

#producao
def server_app():
    app.register_blueprint(main)
    print('Rodando')
       
    return app

app.run()


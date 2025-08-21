#Flask
from flask import Flask

#Controladores
from Controllers.Auth_controller import auth_bp
from Controllers.Aparato_controller import aparato_bp
from Controllers.Usuario_controller import usuario_bp

app = Flask(__name__)
app.secret_key = "Camino324"

app.register_blueprint(auth_bp)
app.register_blueprint(aparato_bp)
app.register_blueprint(usuario_bp)

if __name__ == '__main__':
    app.run(debug=True)
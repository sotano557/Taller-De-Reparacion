from flask import Blueprint, render_template, request, session, url_for, redirect

from Model.Usuarios import Usuario

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route("/")
def index():
    session["id_user"] = ""
    return render_template("index.html")


@auth_bp.route("/Inicio")
def login():
    userLogin = request.form['email']
    psswdLogin = request.form['password']

    usuario = Usuario()
    resultadoDB = usuario.login(userLogin, psswdLogin)

    if resultadoDB == None:
        error = "Usuario o contraseña incorecta"
        return render_template("index.html", error=error)
    else:
        return render_template("Menu.hmtl")



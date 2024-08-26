
from app import bd
from flask import request, jsonify, render_template, Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET'])
def pagina_login():
    return render_template('cadastro.html')


@auth.route('/registrar', methods=['POST',])
def registrar():
    email = request.form['email']
    senha = request.form['senha']
    new_user = User(email, senha)
    try:
        bd.session.add(new_user)
        bd.session.commit()
        return 'Cadastro feito com sucesso', 201
    except Exception as e:
        print(e)
        return 'Erro no registro', 400

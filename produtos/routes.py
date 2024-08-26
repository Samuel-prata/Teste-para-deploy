from flask import Flask, jsonify, render_template, request, Blueprint
from config import Config
from produtos.models import bd, Produto

produto = Blueprint('produto', __name__, url_prefix='/produto')


@produto.route('/', methods=['POST', 'GET'])
def hello():
    return jsonify()


@produto.route('/registrar', methods=['POST'])
def registrar():
    dados = request.get_json()
    novo_produto = Produto(nome=dados['nome'], categoria=dados['categoria'],
                           preco=dados['preco'], quantidade=dados['quantidade'])
    try:
        bd.session.add(novo_produto)
        bd.session.commit()
        return f'Produto cadastrado com sucesso', 201
    except Exception as e:
        print(e)
        return f'Erro ao cadastrar produto', 400


@produto.route('/consultar')
def consultar_todos():
    # Versão atualizada
    produtos = bd.session.execute(bd.select(Produto)).scalars().all()
    dados_json = [produto.to_dict() for produto in produtos]
    import os
    print("url: ", os.getenv('DATABASE_URL_DEV'))
    print("url: ", os.getenv('DATABASE_URL_PROD'))
    return jsonify(dados_json)


@produto.route('/consultar/<int:id>')
def get_id(id):
    select_query = bd.select(Produto).where(Produto.id == id)
    produto = bd.session.execute(select_query).scalar_one_or_none()
    print(type(produto))
    if produto is None:
        return f'Produto não encontrado', 404
    else:
        return jsonify(produto.to_dict()), 200


@produto.route('/atualizar/<int:id>', methods=['PUT'])
def atualizar(id):
    produto = encontrar(id)
    dados_atualizados = request.get_json()

    try:
        produto.nome = dados_atualizados['nome']
        produto.categoria = produto.categoria
        produto.preco = dados_atualizados['preco']
        produto.quantidade = dados_atualizados['quantidade']
        bd.session.add(produto)
        bd.session.commit()
        return f'Atualizado com sucesso', 200
    except Exception as e:
        print(e)
        return f' Erro ao cadastrar', 400


@produto.route('/deletar/<int:id>', methods=['DELETE'])
def deletar(id):
    produto = encontrar(id)
    try:
        bd.session.delete(produto)
        bd.session.commit()
        return 'Produto deletado', 200
    except Exception as e:
        print(e)
        return f'Erro ao deletar produto', 400


def encontrar(id):
    select_id = bd.select(Produto).where(Produto.id == id)
    produto = bd.session.execute(select_id).scalar_one()
    return produto


@produto.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template('erro.html'), 404

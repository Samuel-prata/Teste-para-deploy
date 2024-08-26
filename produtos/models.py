# Criar um modelo para o banco de dados

from app import bd


class Produto(bd.Model):
    __tablename__ = 'produtos'
  # nome_da coluna = variavel.Column( bd.Tipo_de_dado, constraint)
    id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(200))  # -> VARCHAR(200)
    categoria = bd.Column(bd.String(100))
    preco = bd.Column(bd.Float)
    quantidade = bd.Column(bd.Integer)

    def __init__(self, nome, categoria, preco, quantidade):
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            'nome': self.nome,
            'categoria': self.categoria,
            'preço': self.preco,
            'quantidade': self.quantidade
        }

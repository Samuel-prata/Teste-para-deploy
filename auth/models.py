from app import bd

class User(bd.Model):
    __tablename__ = "tb_users"

    id = bd.Column(bd.Integer, primary_key=True)
    email = bd.Column(bd.String(100))
    senha = bd.Column(bd.String(100))

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha

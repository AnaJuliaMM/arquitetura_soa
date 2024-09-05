from flask_sqlalchemy import SQLAlchemy

# Instancia o objeto SQLAlchemy que será usado para definir e gerenciar o banco de dados
db = SQLAlchemy()

class User(db.Model):
    """
    Modelo que representa um usuário no banco de dados.

    Atributos:
    - id: Identificador único do usuário (chave primária).
    - name: Nome do usuário.
    - email: Email do usuário (deve ser único).

    Métodos:
    - to_dict: Converte a instância do usuário em um dicionário.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        """
        Converte a instância do User em um dicionário.

        Retorna:
        dict: Representação do usuário com os campos 'id', 'name' e 'email'.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

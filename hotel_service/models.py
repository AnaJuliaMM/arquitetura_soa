from flask_sqlalchemy import SQLAlchemy

# Instancia o objeto SQLAlchemy que será usado para definir e gerenciar o banco de dados
db = SQLAlchemy()

class Hotel(db.Model):
    """
    Modelo que representa um hotel no banco de dados.

    Atributos:
    - id: Identificador único do hotel (chave primária).
    - name: Nome do hotel.
    - location: Localização do hotel.

    Métodos:
    - to_dict: Converte a instância do hotel em um dicionário.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    location = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        """
        Converte a instância do Hotel em um dicionário.

        Retorna:
        dict: Representação do hotel com os campos 'id', 'name' e 'location'.
        """
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }

class Review(db.Model):
    """
    Modelo que representa uma avaliação de um hotel no banco de dados.

    Atributos:
    - id: Identificador único da avaliação (chave primária).
    - hotel_id: Identificador do hotel ao qual a avaliação pertence (chave estrangeira).
    - rating: Avaliação do hotel (nota).
    - review_text: Texto da avaliação.

    Relacionamentos:
    - hotel: Relaciona a avaliação com o hotel correspondente.

    Métodos:
    - to_dict: Converte a instância da avaliação em um dicionário.
    """
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, db.ForeignKey('hotel.id'), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    review_text = db.Column(db.String(500), nullable=True)

    hotel = db.relationship('Hotel', backref=db.backref('reviews', lazy=True))

    def to_dict(self):
        """
        Converte a instância da Review em um dicionário.

        Retorna:
        dict: Representação da avaliação com os campos 'id', 'hotel_id', 'rating' e 'review_text'.
        """
        return {
            'id': self.id,
            'hotel_id': self.hotel_id,
            'rating': self.rating,
            'review_text': self.review_text
        }

class Reservation(db.Model):
    """
    Modelo que representa uma reserva de hotel no banco de dados.

    Atributos:
    - id: Identificador único da reserva (chave primária).
    - user_id: Identificador do usuário que fez a reserva.
    - hotel_id: Identificador do hotel reservado.
    - date: Data da reserva.

    Métodos:
    - to_dict: Converte a instância da reserva em um dicionário.
    """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    hotel_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        """
        Converte a instância da Reservation em um dicionário.

        Retorna:
        dict: Representação da reserva com os campos 'id', 'user_id', 'hotel_id' e 'date'.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'hotel_id': self.hotel_id,
            'date': self.date
        }

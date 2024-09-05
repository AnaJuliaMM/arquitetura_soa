from flask import Flask, Response, request
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Float, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from models import db, Hotel, Review, Reservation

# Cria uma instância da aplicação Flask
app = Flask(__name__)
# Configura a URI do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
# Inicializa o objeto SQLAlchemy com a aplicação Flask
db.init_app(app)

class HotelService(ServiceBase):
    """
    Serviço SOAP que fornece operações relacionadas a hotéis, avaliações e reservas.

    Métodos:
    - get_hotels: Retorna uma lista de todos os hotéis.
    - get_hotel: Retorna os detalhes de um hotel específico pelo ID.
    - add_hotel: Adiciona um novo hotel com o nome e localização fornecidos.
    - get_reviews: Retorna uma lista de avaliações para um hotel específico.
    - get_review: Retorna os detalhes de uma avaliação específica pelo ID.
    - add_review: Adiciona uma nova avaliação para um hotel com a nota e o texto fornecidos.
    - get_reservations: Retorna uma lista de todas as reservas.
    - get_reservation: Retorna os detalhes de uma reserva específica pelo ID.
    - add_reservation: Adiciona uma nova reserva com o ID do usuário, ID do hotel e a data fornecida.
    """

    @rpc(_returns=Iterable(Unicode))
    def get_hotels(ctx):
        """
        Obtém uma lista de todos os hotéis.

        Retorna:
        Iterable[Unicode]: Lista de hotéis no formato de dicionário.
        """
        hotels = Hotel.query.all()
        return [str(hotel.to_dict()) for hotel in hotels]

    @rpc(Integer, _returns=Unicode)
    def get_hotel(ctx, id):
        """
        Obtém os detalhes de um hotel específico pelo ID.

        Parâmetros:
        - id (Integer): ID do hotel.

        Retorna:
        Unicode: Detalhes do hotel no formato de dicionário.
        """
        hotel = Hotel.query.get_or_404(id)
        return str(hotel.to_dict())

    @rpc(Unicode, Unicode, _returns=Unicode)
    def add_hotel(ctx, name, location):
        """
        Adiciona um novo hotel com o nome e localização fornecidos.

        Parâmetros:
        - name (Unicode): Nome do hotel.
        - location (Unicode): Localização do hotel.

        Retorna:
        Unicode: Detalhes do hotel adicionado no formato de dicionário.
        """
        new_hotel = Hotel(name=name, location=location)
        db.session.add(new_hotel)
        db.session.commit()
        return str(new_hotel.to_dict())

    @rpc(Integer, _returns=Iterable(Unicode))
    def get_reviews(ctx, hotel_id):
        """
        Obtém uma lista de avaliações para um hotel específico.

        Parâmetros:
        - hotel_id (Integer): ID do hotel.

        Retorna:
        Iterable[Unicode]: Lista de avaliações no formato de dicionário.
        """
        reviews = Review.query.filter_by(hotel_id=hotel_id).all()
        return [str(review.to_dict()) for review in reviews]

    @rpc(Integer, _returns=Unicode)
    def get_review(ctx, id):
        """
        Obtém os detalhes de uma avaliação específica pelo ID.

        Parâmetros:
        - id (Integer): ID da avaliação.

        Retorna:
        Unicode: Detalhes da avaliação no formato de dicionário.
        """
        review = Review.query.get_or_404(id)
        return str(review.to_dict())

    @rpc(Integer, Float, Unicode, _returns=Unicode)
    def add_review(ctx, hotel_id, rating, review_text):
        """
        Adiciona uma nova avaliação para um hotel com a nota e o texto fornecidos.

        Parâmetros:
        - hotel_id (Integer): ID do hotel.
        - rating (Float): Nota da avaliação.
        - review_text (Unicode): Texto da avaliação.

        Retorna:
        Unicode: Detalhes da avaliação adicionada no formato de dicionário.
        """
        new_review = Review(hotel_id=hotel_id, rating=rating, review_text=review_text)
        db.session.add(new_review)
        db.session.commit()
        return str(new_review.to_dict())

    @rpc(_returns=Iterable(Unicode))
    def get_reservations(ctx):
        """
        Obtém uma lista de todas as reservas.

        Retorna:
        Iterable[Unicode]: Lista de reservas no formato de dicionário.
        """
        reservations = Reservation.query.all()
        return [str(reservation.to_dict()) for reservation in reservations]

    @rpc(Integer, _returns=Unicode)
    def get_reservation(ctx, id):
        """
        Obtém os detalhes de uma reserva específica pelo ID.

        Parâmetros:
        - id (Integer): ID da reserva.

        Retorna:
        Unicode: Detalhes da reserva no formato de dicionário.
        """
        reservation = Reservation.query.get_or_404(id)
        return str(reservation.to_dict())

    @rpc(Integer, Integer, Unicode, _returns=Unicode)
    def add_reservation(ctx, user_id, hotel_id, date):
        """
        Adiciona uma nova reserva com o ID do usuário, ID do hotel e a data fornecidos.

        Parâmetros:
        - user_id (Integer): ID do usuário.
        - hotel_id (Integer): ID do hotel.
        - date (Unicode): Data da reserva.

        Retorna:
        Unicode: Detalhes da reserva adicionada no formato de dicionário.
        """
        new_reservation = Reservation(user_id=user_id, hotel_id=hotel_id, date=date)
        db.session.add(new_reservation)
        db.session.commit()
        return str(new_reservation.to_dict())

# Configura o serviço SOAP com o serviço HotelService
soap_app = Application(
    [HotelService],
    'spyne.examples.hotel',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

# Cria uma instância do WsgiApplication para o serviço SOAP
wsgi_app = WsgiApplication(soap_app)

@app.route('/soap', methods=['GET', 'POST'])
def soap():
    """
    Manipula as requisições SOAP para o endpoint /soap.

    - Para requisições GET: Retorna o WSDL do serviço SOAP.
    - Para requisições POST: Processa as mensagens SOAP e retorna a resposta.

    Retorna:
    Response: Resposta HTTP com o WSDL ou a resposta SOAP, dependendo do método da requisição.
    """
    if request.method == 'GET':
        # Manipula requisições WSDL
        environ = request.environ
        start_response = lambda status, headers: None
        wsdl_response = wsgi_app(environ, start_response)
        return Response(wsdl_response, mimetype='text/xml')
    else:
        # Manipula requisições SOAP
        environ = request.environ
        start_response = lambda status, headers: None
        response = wsgi_app(environ, start_response)
        return Response(response, status=200, mimetype='text/xml')

if __name__ == '__main__':
    # Executa o aplicativo Flask na porta 5001
    app.run(port=5001)

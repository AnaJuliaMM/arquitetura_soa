from flask import Flask
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Float, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from models import db, Hotel, Review, Reservation


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db.init_app(app)

class HotelService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def get_hotels(ctx):
        hotels = Hotel.query.all()
        return [str(hotel.to_dict()) for hotel in hotels]

    @rpc(Integer, _returns=Unicode)
    def get_hotel(ctx, id):
        hotel = Hotel.query.get_or_404(id)
        return str(hotel.to_dict())

    @rpc(Unicode, Unicode, _returns=Unicode)
    def add_hotel(ctx, name, location):
        new_hotel = Hotel(name=name, location=location)
        db.session.add(new_hotel)
        db.session.commit()
        return str(new_hotel.to_dict())

    @rpc(Integer, _returns=Iterable(Unicode))
    def get_reviews(ctx, hotel_id):
        reviews = Review.query.filter_by(hotel_id=hotel_id).all()
        return [str(review.to_dict()) for review in reviews]

    @rpc(Integer, _returns=Unicode)
    def get_review(ctx, id):
        review = Review.query.get_or_404(id)
        return str(review.to_dict())

    @rpc(Integer, Float, Unicode, _returns=Unicode)
    def add_review(ctx, hotel_id, rating, review_text):
        new_review = Review(hotel_id=hotel_id, rating=rating, review_text=review_text)
        db.session.add(new_review)
        db.session.commit()
        return str(new_review.to_dict())

    @rpc(_returns=Iterable(Unicode))
    def get_reservations(ctx):
        reservations = Reservation.query.all()
        return [str(reservation.to_dict()) for reservation in reservations]

    @rpc(Integer, _returns=Unicode)
    def get_reservation(ctx, id):
        reservation = Reservation.query.get_or_404(id)
        return str(reservation.to_dict())

    @rpc(Integer, Integer, Unicode, _returns=Unicode)
    def add_reservation(ctx, user_id, hotel_id, date):
        new_reservation = Reservation(user_id=user_id, hotel_id=hotel_id, date=date)
        db.session.add(new_reservation)
        db.session.commit()
        return str(new_reservation.to_dict())

application = Application(
    [HotelService],
    'spyne.examples.hotel',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

soap_app = WsgiApplication(application)

@app.route('/soap', methods=['POST'])
def soap():
    return soap_app.wsgi_app

if __name__ == '__main__':
    app.run(port=5001)

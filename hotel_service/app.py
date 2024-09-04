from flask import Flask, jsonify, request
from models import db, Hotel, Review, Reservation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db.init_app(app)



# Rotas de hotel
@app.route('/hotels', methods=['GET'])
def get_hotels():
    hotels = Hotel.query.all()
    return jsonify([hotel.to_dict() for hotel in hotels])


@app.route('/hotels/<int:id>', methods=['GET'])
def get_hotel(id):
    hotel = Hotel.query.get_or_404(id)
    return jsonify(hotel.to_dict())


@app.route('/hotels', methods=['POST'])
def add_hotel():
    data = request.json
    new_hotel = Hotel(name=data['name'], location=data['location'])
    db.session.add(new_hotel)
    db.session.commit()
    return jsonify(new_hotel.to_dict()), 201



# Rotas de avaliação
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    return jsonify([review.to_dict() for review in reviews])


@app.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    review = Review.query.get_or_404(id)
    return jsonify(review.to_dict())


@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.json
    new_review = Review(
        hotel_id=data['hotel_id'],
        rating=data['rating'],
        review_text=data.get('review_text', '')
    )
    db.session.add(new_review)
    db.session.commit()
    return jsonify(new_review.to_dict()), 201



# Rotas de avaliacao
@app.route('/reservations', methods=['GET'])
def get_reservations():
    reservations = Reservation.query.all()
    return jsonify([reservation.to_dict() for reservation in reservations])

@app.route('/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    reservation = Reservation.query.get_or_404(id)
    return jsonify(reservation.to_dict())

@app.route('/reservations', methods=['POST'])
def add_reservation():
    data = request.json
    new_reservation = Reservation(user_id=data['user_id'], hotel_id=data['hotel_id'], date=data['date'])
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify(new_reservation.to_dict()), 201


# Gerar metricas
def calculate_average_rating(reviews):
    if not reviews:
        return 0
    total_rating = sum(review.rating for review in reviews)
    return total_rating / len(reviews)


@app.route('/hotels/<int:id>/performance', methods=['GET'])
def get_hotel_performance(id):
    hotel = Hotel.query.get_or_404(id)

    # Obter avaliações do hotel
    reviews = Review.query.filter_by(hotel_id=id).all()
    average_rating = calculate_average_rating(reviews)
    reviews_count = len(reviews)

    # Obter reservas do hotel
    reservations = Reservation.query.filter_by(hotel_id=id).all()
    total_reservations = len(reservations)

    # Preparar relatório de desempenho
    performance_report = {
        'hotel': hotel.to_dict(),
        'performance': {
            'average_rating': average_rating,
            'reviews_count': reviews_count,
            'total_reservations': total_reservations
        }
    }

    return jsonify(performance_report)



if __name__ == '__main__':
    app.run(port=5001)

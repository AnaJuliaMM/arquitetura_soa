from flask import Flask, jsonify, request
from models import db, Reservation

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reservation.db'
db.init_app(app)

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

if __name__ == '__main__':
    app.run(port=5002)

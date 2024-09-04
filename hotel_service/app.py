from flask import Flask, jsonify, request
from models import db, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db.init_app(app)

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

if __name__ == '__main__':
    app.run(port=5001)

from flask import Flask, jsonify, request
import zeep

app = Flask(__name__)

HOTELS_SERVICE_URL = 'http://localhost:5001/soap?wsdl'
USERS_SERVICE_URL = 'http://localhost:5003/soap?wsdl'

hotels_client = zeep.Client(HOTELS_SERVICE_URL)
users_client = zeep.Client(USERS_SERVICE_URL)

@app.route('/esb/hotels', methods=['GET'])
def get_hotels():
    response = hotels_client.service.get_hotels()
    return jsonify(response)

@app.route('/esb/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    response = hotels_client.service.get_reservation(id)
    return jsonify(response)

@app.route('/esb/users/<int:id>', methods=['GET'])
def get_user(id):
    response = users_client.service.get_user(id)
    return jsonify(response)

@app.route('/esb/complex-query', methods=['GET'])
def complex_query():
    hotel_id = request.args.get('hotel_id')
    user_id = request.args.get('user_id')
    
    reservations_response = hotels_client.service.get_reservations()
    hotel_response = hotels_client.service.get_hotel(hotel_id)
    user_response = users_client.service.get_user(user_id)
    
    response = {
        'hotel': hotel_response,
        'user': user_response,
        'reservations': reservations_response
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)

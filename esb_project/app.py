from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URLs dos serviços
HOTELS_SERVICE_URL = 'http://localhost:5001'
USERS_SERVICE_URL = 'http://localhost:5003'


# Função para transformar dados (exemplo simples)
def transform_data(data):
    # Adapte conforme necessário para transformar dados entre formatos
    return data



# Roteamento e orquestração
@app.route('/esb/hotels', methods=['GET'])
def get_hotels():
    response = requests.get(f'{HOTELS_SERVICE_URL}/hotels')
    data = response.json()
    transformed_data = transform_data(data)
    return jsonify(transformed_data)

@app.route('/esb/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    response = requests.get(f'{HOTELS_SERVICE_URL}/reservations/{id}')
    data = response.json()
    transformed_data = transform_data(data)
    return jsonify(transformed_data)

@app.route('/esb/users/<int:id>', methods=['GET'])
def get_user(id):
    response = requests.get(f'{USERS_SERVICE_URL}/users/{id}')
    data = response.json()
    transformed_data = transform_data(data)
    return jsonify(transformed_data)

@app.route('/esb/complex-query', methods=['GET'])
def complex_query():
    hotel_id = request.args.get('hotel_id')
    user_id = request.args.get('user_id')
    
    # Consultar o serviço de reservas para obter as reservas
    reservations_response = requests.get(f'{HOTELS_SERVICE_URL}/reservations', params={'hotel_id': hotel_id, 'user_id': user_id})
    reservations_data = reservations_response.json()
    
    # Consultar o serviço de hotéis e usuários
    hotel_response = requests.get(f'{HOTELS_SERVICE_URL}/hotels/{hotel_id}')
    user_response = requests.get(f'{USERS_SERVICE_URL}/users/{user_id}')
    
    hotel_data = hotel_response.json()
    user_data = user_response.json()
    
    # Combinar dados para fornecer uma resposta consolidada
    response = {
        'hotel': hotel_data,
        'user': user_data,
        'reservations': reservations_data
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)

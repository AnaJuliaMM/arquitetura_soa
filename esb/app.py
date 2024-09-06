from flask import Flask, jsonify, request
import zeep

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# URLs dos serviços SOAP que serão consumidos
HOTELS_SERVICE_URL = 'http://localhost:5001/soap?wsdl'
USERS_SERVICE_URL = 'http://localhost:5003/soap?wsdl'

# Cria clientes SOAP para interagir com os serviços de hotéis e usuários
hotels_client = zeep.Client(HOTELS_SERVICE_URL)
users_client = zeep.Client(USERS_SERVICE_URL)

@app.route('/esb/hotels', methods=['GET'])
def get_hotels():
    """
    Obtém uma lista de todos os hotéis usando o serviço SOAP de hotéis.

    Retorna:
    Response: Resposta HTTP com a lista de hotéis em formato JSON.
    """
    response = hotels_client.service.get_hotels()
    return jsonify(response)

@app.route('/esb/reservations/<int:id>', methods=['GET'])
def get_reservation(id):
    """
    Obtém os detalhes de uma reserva específica pelo ID usando o serviço SOAP de hotéis.

    Parâmetros:
    - id (int): ID da reserva.

    Retorna:
    Response: Resposta HTTP com os detalhes da reserva em formato JSON.
    """
    response = hotels_client.service.get_reservation(id)
    return jsonify(response)

@app.route('/esb/users/<int:id>', methods=['GET'])
def get_user(id):
    """
    Obtém os detalhes de um usuário específico pelo ID usando o serviço SOAP de usuários.

    Parâmetros:
    - id (int): ID do usuário.

    Retorna:
    Response: Resposta HTTP com os detalhes do usuário em formato JSON.
    """
    response = users_client.service.get_user(id)
    return jsonify(response)


if __name__ == '__main__':
    # Executa o aplicativo Flask na porta 5000
    app.run(port=5000)

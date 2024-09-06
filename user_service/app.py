from flask import Flask, Response, request
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from models import db, User

# Cria uma instância da aplicação Flask
app = Flask(__name__)
# Configura a URI do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
# Inicializa o objeto SQLAlchemy com a aplicação Flask
db.init_app(app)

class UserService(ServiceBase):
    """
    Serviço SOAP que fornece operações relacionadas a usuários.

    Métodos:
    - get_users: Retorna uma lista de todos os usuários.
    - get_user: Retorna os detalhes de um usuário específico pelo ID.
    - add_user: Adiciona um novo usuário com o nome e email fornecidos.
    """

    @rpc(_returns=Iterable(Unicode))
    def get_users(ctx):
        """
        Obtém uma lista de todos os usuários.

        Retorna:
        Iterable[Unicode]: Lista de usuários no formato de dicionário.
        """
        users = User.query.all()
        return [str(user.to_dict()) for user in users]

    @rpc(Integer, _returns=Unicode)
    def get_user(ctx, id):
        """
        Obtém os detalhes de um usuário específico pelo ID.

        Parâmetros:
        - id (Integer): ID do usuário.

        Retorna:
        Unicode: Detalhes do usuário no formato de dicionário.
        """
        user = User.query.get_or_404(id)
        return str(user.to_dict())

    @rpc(Unicode, Unicode, _returns=Unicode)
    def add_user(ctx, name, email):
        """
        Adiciona um novo usuário com o nome e email fornecidos.

        Parâmetros:
        - name (Unicode): Nome do usuário.
        - email (Unicode): Email do usuário.

        Retorna:
        Unicode: Detalhes do usuário adicionado no formato de dicionário.
        """
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return str(new_user.to_dict())

# Configura o serviço SOAP com o serviço UserService
soap_app = Application(
    [UserService],
    'spyne.examples.user',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

# Cria uma instância do WsgiApplication para o serviço SOAP
wsgi_app = WsgiApplication(soap_app)

@app.route('/soap', methods=['GET', 'POST'])
def soap():
    """
    Manipula as requisições SOAP para o endpoint /soap.

    - Para requisições GET: Retorna o WSDL (Web Services Description Language) do serviço SOAP.
    - Para requisições POST: Processa as mensagens SOAP enviadas ao serviço e retorna a resposta.

    Retorna:
    Response: Resposta HTTP contendo o WSDL ou a resposta SOAP, dependendo do método da requisição.
    """
    # Verifica se a requisição é do tipo GET
    if request.method == 'GET':
        # Obtém o ambiente da requisição atual
        environ = request.environ
        # Define uma função de resposta vazia (para ser usada pelo WSGI)
        start_response = lambda status, headers: None
        # Chama a aplicação WSGI para gerar a resposta WSDL
        wsdl_response = wsgi_app(environ, start_response)
        # Retorna o WSDL em formato XML como resposta HTTP
        return Response(wsdl_response, mimetype='text/xml')
    else:
        # Se não for GET, manipula as requisições SOAP (normalmente são requisições POST)
        # Obtém o ambiente da requisição atual
        environ = request.environ
        # Define uma função de resposta vazia (para ser usada pelo WSGI)
        start_response = lambda status, headers: None
        # Chama a aplicação WSGI para processar a requisição SOAP
        response = wsgi_app(environ, start_response)
        # Retorna a resposta SOAP processada em formato XML
        return Response(response, status=200, mimetype='text/xml')


if __name__ == '__main__':
    # Executa o aplicativo Flask na porta 5003
    app.run(port=5003)

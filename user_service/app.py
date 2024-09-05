from flask import Flask, Response, request
from spyne import Application, rpc, ServiceBase, Integer, Unicode, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db.init_app(app)

class UserService(ServiceBase):
    @rpc(_returns=Iterable(Unicode))
    def get_users(ctx):
        users = User.query.all()
        return [str(user.to_dict()) for user in users]

    @rpc(Integer, _returns=Unicode)
    def get_user(ctx, id):
        user = User.query.get_or_404(id)
        return str(user.to_dict())

    @rpc(Unicode, Unicode, _returns=Unicode)
    def add_user(ctx, name, email):
        new_user = User(name=name, email=email)
        db.session.add(new_user)
        db.session.commit()
        return str(new_user.to_dict())

soap_app = Application(
    [UserService],
    'spyne.examples.user',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

@app.route('/soap', methods=['GET', 'POST'])
def soap():
    if request.method == 'GET':
        # Handle WSDL requests
        environ = request.environ
        start_response = lambda status, headers: None
        wsdl_response = wsgi_app(environ, start_response)
        return Response(wsdl_response, mimetype='text/xml')
    else:
        # Handle SOAP requests
        environ = request.environ
        start_response = lambda status, headers: None
        response = wsgi_app(environ, start_response)
        return Response(response, status=200, mimetype='text/xml')

if __name__ == '__main__':
    app.run(port=5003)

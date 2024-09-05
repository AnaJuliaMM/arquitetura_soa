from flask import Flask
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

application = Application(
    [UserService],
    'spyne.examples.user',
    in_protocol=Soap11(),
    out_protocol=Soap11()
)

soap_app = WsgiApplication(application)

@app.route('/soap', methods=['POST'])
def soap():
    return soap_app.wsgi_app

if __name__ == '__main__':
    app.run(port=5003)

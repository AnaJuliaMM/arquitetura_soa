from app import app, db
# from models import Hotel

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso.")

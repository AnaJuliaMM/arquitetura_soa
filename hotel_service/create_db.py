"""
Este script é responsável por criar todas as tabelas definidas nos modelos do SQLAlchemy no banco de dados.

Funcionalidade:
1. Configura o contexto da aplicação Flask usando `app.app_context()`.
2. Usa `db.create_all()` para criar as tabelas no banco de dados conforme definido nos modelos do SQLAlchemy.
3. Imprime uma mensagem de sucesso indicando que as tabelas foram criadas com sucesso.

É importante garantir que a aplicação Flask e a configuração do banco de dados estejam corretamente configuradas antes de executar este script.
"""

from app import app, db

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso.")

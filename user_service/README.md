# Flask Reservation API

Uma API simples para gerenciar reservas usando Flask e SQLite. A API permite obter uma lista de reservas, obter informações sobre uma reserva específica e adicionar novas reservas.

## Tecnologias Utilizadas

- [Flask](https://flask.palletsprojects.com/) - Micro framework para criação de aplicações web.
- [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) - Extensão para integração do Flask com SQLAlchemy e bancos de dados.
- [SQLite](https://www.sqlite.org/) - Banco de dados SQL leve, usado para armazenamento de dados.

## Estrutura do Projeto
hotel_service/ 
├── app.py # Arquivo principal da aplicação Flask 
├── models.py # Define os modelos de dados e a configuração do banco de dados 
├── create_db.py # Script para instanciar o bando de dados 
├── requirements.txt # Depêndencias da API 
└── venv/ # Ambiente virtual (opcional)

## Configuração do Ambiente

### Pré-requisitos

- Python 3.11 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório:**

   ```sh
   git clone <url>
   cd flask_hotel_api
   ```

2. **Crie e ative um ambiente virtual (opcional, mas recomendado):**

   ```sh
   python -m venv venv
   ```

   Ative o ambiente virtual:

   *No Windows:*
   ```sh
   venv\Scripts\activate
   ```
   
   *No macOS/Linux:*
   ```sh
   source venv/bin/activate
   ```

3. **Instale as dependências do projeto:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Inicialize o banco de dados:**
   ```sh
   python create_db.py
   ```

### Execução

Para iniciar o servidor Flask, execute o seguinte comando:

   ```sh
   python app.py
   ```
A API estará disponível em ***http://127.0.0.1:5001***.

## Endpoints

### Obter todos os hotéis

- URL: */users*
- Método: GET
- Resposta:
   ```sh
    [
        {
            "id": 1,
            "name": "Felipe Andrade",
            "email": "felipe_andrade@example.com"
        }
    ]
   ```

### Obter um hotel específico

- URL: */users/<id>*
- Método: GET
- Parâmetros:
   - *id* (int) - ID do usuário
- Resposta:
   ```sh
    {
    "id": 1,
    "name": "Felipe Andrade",
    "email": "felipe_andrade@example.com"
    }
   ```

### Adicionar um novo hotel

- URL: */users*
- Método: POST
- Corpo da Requisição:
   ```sh
    {
        "name": "Felipe Andrade",
        "email": "felipe_andrade@example.com"
    }
   ```
- Resposta:
   ```sh
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com"
    }
   ```

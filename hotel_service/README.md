# Flask Hotel API

Uma API simples para gerenciar informações sobre hotéis usando Flask e SQLite. A API permite obter uma lista de hotéis, obter informações sobre um hotel específico e adicionar novos hotéis.

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

- URL: */hotels*
- Método: GET
- Resposta:
   ```sh
   [
    {
        "id": 1,
        "name": "Hotel California",
        "location": "California"
    }
   ]
   ```

### Obter um hotel específico

- URL: */hotels/<id>*
- Método: GET
- Parâmetros:
   - *id* (int) - ID do hotel
- Resposta:
   ```sh
   {
      "id": 1,
      "name": "Hotel California",
      "location": "California"
   }
   ```

### Adicionar um novo hotel

- URL: */hotels*
- Método: POST
- Corpo da Requisição:
   ```sh
   {
      "name": "Nome do Hotel",
      "location": "Localização do Hotel"
   }
   ```
- Resposta:
   ```sh
   {
      "id": 1,
      "name": "Nome do Hotel",
      "location": "Localização do Hotel"
   }
   ```

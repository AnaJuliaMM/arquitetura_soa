# User Management SOAP API

Este é um aplicativo de gerenciamento de usuários que fornece uma API SOAP usando Flask e Spyne. A aplicação permite a gestão de usuários por meio de operações SOAP.

## Tecnologias Utilizadas

- Python 3.6 ou superior
- Flask
- Spyne
- SQLAlchemy
- SQLite


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
A API estará disponível em ***http://127.0.0.1:5003***.


## Endpoints SOAP

### `get_users`

- **Método:** `GET`
- **Retorno:** Lista de todos os usuários.

### `get_user(id)`

- **Método:** `GET`
- **Parâmetro:** `id` (ID do usuário)
- **Retorno:** Detalhes do usuário especificado.

### `add_user(name, email)`

- **Método:** `POST`
- **Parâmetros:** `name` (Nome do usuário), `email` (Email do usuário)
- **Retorno:** Detalhes do usuário adicionado.

## Rota WSDL (para debugg)

Para visualizar o acordo WSDL, acesse o seguinte endpoint:

- **Rota:** `/soap?wsdl`
- **Retorno:** Documentação do serviço em XML

## Modelos

O aplicativo utiliza o seguinte modelo:

- **User:** Representa um usuário com `id`, `name` e `email`.


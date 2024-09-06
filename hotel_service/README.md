# Hotel Management SOAP API

Este é um aplicativo de gerenciamento de hotéis que fornece uma API SOAP usando Flask e Spyne. A aplicação permite a gestão de hotéis, avaliações e reservas por meio de operações SOAP.

## Requisitos

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
   cd hotel_service
   ```

2. **Crie e ative um ambiente virtual:**

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

## Endpoint SOAP


### `get_hotels`

- **Método:** `GET`
- **Retorno:** Lista de todos os hotéis.

### `get_hotel(id)`

- **Método:** `GET`
- **Parâmetro:** `id` (ID do hotel)
- **Retorno:** Detalhes do hotel especificado.

### `add_hotel(name, location)`

- **Método:** `POST`
- **Parâmetros:** `name` (Nome do hotel), `location` (Localização do hotel)
- **Retorno:** Detalhes do hotel adicionado.

### `get_reviews(hotel_id)`

- **Método:** `GET`
- **Parâmetro:** `hotel_id` (ID do hotel)
- **Retorno:** Lista de avaliações para o hotel especificado.

### `get_review(id)`

- **Método:** `GET`
- **Parâmetro:** `id` (ID da avaliação)
- **Retorno:** Detalhes da avaliação especificada.

### `add_review(hotel_id, rating, review_text)`

- **Método:** `POST`
- **Parâmetros:** `hotel_id` (ID do hotel), `rating` (Classificação), `review_text` (Texto da avaliação)
- **Retorno:** Detalhes da avaliação adicionada.

### `get_reservations`

- **Método:** `GET`
- **Retorno:** Lista de todas as reservas.

### `get_reservation(id)`

- **Método:** `GET`
- **Parâmetro:** `id` (ID da reserva)
- **Retorno:** Detalhes da reserva especificada.

### `add_reservation(user_id, hotel_id, date)`

- **Método:** `POST`
- **Parâmetros:** `user_id` (ID do usuário), `hotel_id` (ID do hotel), `date` (Data da reserva)
- **Retorno:** Detalhes da reserva adicionada.

## Rota WSDL (para debugg)

Para visualizar o acordo WSDL, acesse o seguinte endpoint:

- **Rota:** `/soap?wsdl`
- **Retorno:** Documentação do serviço em XML


## Modelos

O aplicativo utiliza os seguintes modelos:

- **Hotel:** Representa um hotel com `id`, `name` e `location`.
- **Review:** Representa uma avaliação com `id`, `hotel_id`, `rating` e `review_text`.
- **Reservation:** Representa uma reserva com `id`, `user_id`, `hotel_id` e `date`.

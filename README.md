# Seminário de Arquitetura de Software - Arquitetura de Software Orientada a Serviços (SOA)

Este é um sistema simples de reserva de hotel desenvolvido em Python utilizando o framework Flask, demonstrando os princípios da Arquitetura Orientada a Serviços (SOA).

## 1. Explicação Teórica da Arquitetura

A Arquitetura Orientada a Serviços (SOA) é um modelo de design de software que organiza e utiliza serviços desacoplados para fornecer funcionalidades ao sistema. A SOA permite que componentes de software, chamados de serviços, se comuniquem uns com os outros através de uma rede, independentemente das plataformas subjacentes e dos protocolos de comunicação.

## 2. Implementação Prática

Este projeto apresenta um exemplo prático (simples e ilustrativo) de implementação da SOA através de um sistema de reserva de quartos de hotel utilizando Flask.

## 3. Estrutura do Projeto
arquitetura_soa
|_ esb: Enterprise Service Bus (ESB)
|_ hotel_service: Serviço de gerenciamento de hotéis
|_ user_service: Serviço de gerenciamento de usuários


### Tecnologias Utilizadas:
- **Python**: Linguagem de programação.
- **Flask**: Framework web para Python.

### Como Executar o Projeto:
1. Clone este repositório:

```bash
   git clone https://github.com/usuario/arquitetura_soa.git
```

2. Ative os serviços em API Flask seguindo o tutorial contido em cada diretório:
- [Serviço de gerenciamento de hotel](hotel_service/README.md)
- [Serviço de gerenciamento de usuário](user_service/README.md)


3. Assim que os serviços estiverem disponíveis, ative o ESB:
```bash
   cd esb
   python app.py
```

## 4. Endpoints SOAP do ESB (versão 1.0)

### `GET /esb/hotels`

- **Descrição:** Obtém uma lista de todos os hotéis.
- **Resposta:** Lista de hotéis em formato JSON.

### `GET /esb/reservations/<int:id>`

- **Descrição:** Obtém detalhes de uma reserva específica pelo ID.
- **Parâmetro:** `id` (ID da reserva)
- **Resposta:** Detalhes da reserva em formato JSON.

### `GET /esb/users/<int:id>`

- **Descrição:** Obtém detalhes de um usuário específico pelo ID.
- **Parâmetro:** `id` (ID do usuário)
- **Resposta:** Detalhes do usuário em formato JSON.

### `GET /esb/complex-query`

- **Descrição:** Realiza uma consulta complexa que retorna detalhes de um hotel, um usuário e todas as reservas.
- **Parâmetros:**
  - `hotel_id` (ID do hotel)
  - `user_id` (ID do usuário)
- **Resposta:** Objeto JSON contendo detalhes do hotel, do usuário e das reservas.
   

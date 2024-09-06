# Enterprise Service Bus (ESB) na Arquitetura SOA

Este projeto é um exemplo de como um Enterprise Service Bus (ESB) pode ser implementado em uma arquitetura Orientada a Serviços (SOA) utilizando Flask e Zeep. O ESB atua como um intermediário que facilita a comunicação entre diferentes serviços em uma arquitetura SOA.

## O que é um ESB?

O **Enterprise Service Bus (ESB)** é uma arquitetura de middleware que promove a integração e a comunicação entre diferentes aplicações e serviços em uma arquitetura SOA (Service-Oriented Architecture). O ESB fornece um mecanismo centralizado para o roteamento, transformação e gerenciamento das mensagens trocadas entre serviços. Ele oferece suporte para:

- **Integração de Serviços:** Conecta serviços e aplicações diferentes, independentemente das tecnologias e protocolos usados.
- **Transformação de Mensagens:** Converte dados entre diferentes formatos e protocolos.
- **Roteamento de Mensagens:** Direciona mensagens para os serviços apropriados com base em regras de negócios.
- **Gerenciamento de Mensagens:** Monitora e gerencia o tráfego de mensagens para garantir a segurança e a integridade dos dados.

## O Projeto

Este projeto demonstra um ESB que integra dois serviços SOAP:

1. **Serviço de Hotéis** (executando na URL `http://localhost:5001/soap?wsdl`)
2. **Serviço de Usuários** (executando na URL `http://localhost:5003/soap?wsdl`)

O ESB expõe uma API REST que interage com esses serviços SOAP e fornece funcionalidades para obter informações sobre hotéis, usuários e reservas, além de realizar consultas mais complexas.

## Endpoints da API do ESB

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

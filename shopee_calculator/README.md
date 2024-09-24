# Shopee Calculator

Este é um sistema simples para calcular o valor mínimo de venda de um produto na Shopee, considerando as taxas aplicadas pela plataforma. O sistema permite que você insira o valor de compra do produto e um valor de venda proposto para verificar se haverá lucro ou prejuízo.

## Funcionalidades

- Calcula o valor mínimo necessário de venda para evitar prejuízo.
- Permite verificar se o valor proposto de venda gerará lucro ou prejuízo.

## Requisitos

Antes de começar, você precisará ter as seguintes ferramentas instaladas:

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [Flask](https://flask.palletsprojects.com/)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seuusuario/shopee_calculator.git
   cd shopee_calculator

2. Crie um ambiente virtual (opcional, mas recomendado):

   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:

    pip install -r requirements.txt

## Executando projeto localmente

Para rodar o servidor Flask localmente, execute o comando:

    python app.py

O servidor estará disponível em http://127.0.0.1:5000/. Acesse este endereço no seu navegador para usar a aplicação.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    lucro = None
    valor_venda_proposto = None
    valor_minimo_venda = None
    valor_recebido = None  # Variável para armazenar o valor recebido

    if request.method == 'POST':
        valor_compra = float(request.form['valor_compra'])
        valor_venda_proposto = request.form.get('valor_venda')

        # Calcula as taxas
        comissao = 0.185
        transacao = 0.015
        taxa_fixa = 4.0

        # Calcula o valor mínimo necessário para não ter prejuízo
        valor_minimo_venda = (valor_compra + taxa_fixa) / (1 - (comissao + transacao))

        if valor_venda_proposto:
            valor_venda_proposto = float(valor_venda_proposto)
            # Calcula o lucro ou prejuízo com o valor de venda proposto
            total_taxas = (valor_venda_proposto * (comissao + transacao)) + taxa_fixa
            lucro = valor_venda_proposto - valor_compra - total_taxas
            # Calcula o valor recebido da Shopee
            valor_recebido = valor_venda_proposto - total_taxas

    return render_template('index.html', valor_minimo_venda=valor_minimo_venda, lucro=lucro, valor_venda_proposto=valor_venda_proposto, valor_recebido=valor_recebido)

if __name__ == '__main__':
    app.run(debug=True)

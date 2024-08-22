from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos disponíveis
produtos = [
    {"id": 1, "nome": "Bloco H4", "preco": 36.0, "unidade": "metro quadrado"},
    {"id": 2, "nome": "Bloco H6", "preco": 40.0, "unidade": "metro quadrado"},
    {"id": 3, "nome": "16 faces h6", "preco": 42.0, "unidade": "metro quadrado"},
    {"id": 4, "nome": "Meio fio rua 1,00x0,30x0,08x0,10", "preco": 16.0, "unidade": "unidade"},
    {"id": 5, "nome": "Meio fio rua 1,00x0,30x0,10x0,12", "preco": 18.0, "unidade": "unidade"},
    {"id": 6, "nome": "Meio fio rua jardim 1,00x0,20x0,05x0,15", "preco": 12.0, "unidade": "unidade"}
]

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/pedido', methods=['POST'])
def pedido():
    produto_id = int(request.form['produto'])
    quantidade = float(request.form['quantidade'])
    unidade = request.form['unidade']

    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if produto:
        if produto['unidade'] == 'metro quadrado':
            total = produto['preco'] * quantidade
        else:
            total = produto['preco'] * quantidade
        return render_template('pedido.html', produto=produto, quantidade=quantidade, total=total, unidade=unidade)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
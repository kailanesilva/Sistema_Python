from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pedidos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Definição do modelo de Pedido
class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_nome = db.Column(db.String(100), nullable=False)
    quantidade = db.Column(db.Float, nullable=False)
    unidade = db.Column(db.String(50), nullable=False)
    total = db.Column(db.Float, nullable=False)

# Criação do banco de dados
with app.app_context():
    db.create_all()

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
        total = produto['preco'] * quantidade
        pedido = Pedido(produto_nome=produto['nome'], quantidade=quantidade, unidade=unidade, total=total)
        db.session.add(pedido)
        db.session.commit()
        return render_template('pedido.html', produto=produto, quantidade=quantidade, total=total, unidade=unidade)
    else:
        return redirect(url_for('index'))

@app.route('/pedidos')
def lista_pedidos():
    pedidos = Pedido.query.all()
    return render_template('lista_pedidos.html', pedidos=pedidos)

@app.route('/limpar_pedidos', methods=['POST'])
def limpar_pedidos():
    Pedido.query.delete()  # Remove todos os pedidos
    db.session.commit()
    return redirect(url_for('lista_pedidos'))

if __name__ == '__main__':
    app.run(debug=True)
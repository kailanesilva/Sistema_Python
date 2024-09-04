# Importando as bibliotecas necessárias
from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Carregar dados de perguntas frequentes

faq_data = pd.read_csv('data/questoes.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/faq')
def faq():
    faqs = faq_data.to_dict(orient='records')
    return jsonify(faqs)

@app.route('/schedule', methods=['POST'])
def schedule():
    name = request.form.get('name')
    email = request.form.get('email')
    date = request.form.get('date')
    return f"Visita agendada para {name} no dia {date}."

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
from firestore_db import listar_inventario
from demand_prediction import prever_demanda

app = Flask(__name__)

# Rota para listar o inventário
@app.route('/api/inventario', methods=['GET'])
def inventario():
    inventario = listar_inventario()
    return jsonify(inventario)

# Rota para previsão de demanda
@app.route('/api/previsao', methods=['GET'])
def previsao():
    previsao_demanda = prever_demanda()
    return jsonify({'previsao_demanda': previsao_demanda})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

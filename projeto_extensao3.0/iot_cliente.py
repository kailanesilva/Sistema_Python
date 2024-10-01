import paho.mqtt.client as mqtt
import json

# Configurações do MQTT
broker_url = "broker.mqtt.url"
broker_port = 1883
topic = "inventario/atualizacao"

# Simulação de dados do sensor RFID
def obter_dados_rfid():
    return {
        "produto_id": "12345",
        "quantidade": 10,
        "timestamp": "2024-10-01T10:30:00"
    }

# Callback quando conectar ao broker MQTT
def on_connect(client, userdata, flags, rc):
    print("Conectado ao MQTT Broker")

# Configuração do cliente MQTT
client = mqtt.Client()
client.on_connect = on_connect
client.connect(broker_url, broker_port)

# Publicando os dados dos sensores
dados_rfid = obter_dados_rfid()
client.publish(topic, json.dumps(dados_rfid))
client.loop_forever()

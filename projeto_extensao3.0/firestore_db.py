from google.cloud import firestore

# Inicializando o Firestore
db = firestore.Client()

# Função para salvar dados no Firestore
def salvar_dados_no_firestore(dados_rfid):
    doc_ref = db.collection("inventario").document(dados_rfid['produto_id'])
    doc_ref.set(dados_rfid)

# Função para recuperar dados do inventário
def listar_inventario():
    inventario_ref = db.collection('inventario')
    docs = inventario_ref.stream()
    inventario = {doc.id: doc.to_dict() for doc in docs}
    return inventario

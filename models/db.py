from pymongo import MongoClient

# Configurando a conexão com o MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['boe-app']


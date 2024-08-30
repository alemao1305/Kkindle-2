# backend/database/mongodb_config.py

from pymongo import MongoClient

def get_database():
    # Substitua com a URL de conexão do MongoDB apropriada
    MONGO_URL = "mongodb://localhost:27017"

    client = MongoClient(MONGO_URL)
    # Substitua 'mydatabase' pelo nome do seu banco de dados
    return client['mydatabase']

db = get_database()

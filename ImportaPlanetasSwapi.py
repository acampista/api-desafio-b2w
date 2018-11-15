import requests
from rest_framework.utils import json
import sqlite3

# Conectando com o banco de dados
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Método para buscar planeta por ID em SWAPI
def busca_planeta(ID):
    try:
        req = requests.get('https://swapi.co/api/planets/' + str(ID))
        dicionario = json.loads(req.text)
        return dicionario
    except:
        print('Erro na conexão')

QtdPlanetas = range(1, 62)

for IdPlaneta in QtdPlanetas:
    planeta = busca_planeta(IdPlaneta)

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO planetas_planeta (id_swapi, nome, clima, terreno, QtdAparicoes)
    VALUES (?,?,?,?,?)
    """, (IdPlaneta, planeta['name'], planeta['climate'], planeta['terrain'], len(planeta['films'])))

    conn.commit()

# Mensagem final
print('Planetas importados com sucesso !')

conn.close()
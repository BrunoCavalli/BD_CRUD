import psycopg2 as psycopg
import random
from datetime import datetime, timedelta

def connect_db():
    try:
        conn = psycopg.connect(
            dbname="bruno.cavalli"
        )
        # Define o schema default
        cur = conn.cursor()
        cur.execute("SET search_path TO netflix;")
        conn.commit()
        return conn, cur
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)
        return None, None

conn, cur = connect_db()
if conn is None or cur is None:
    print("Não foi possível conectar ao banco de dados. Encerrando o programa.")
    exit(1)


# Buscar IDs de perfil válidos no banco
with conn.cursor() as cur:
    cur.execute("SELECT IDPerfil FROM Perfil")
    ids_perfis = [row[0] for row in cur.fetchall()]

# Função para gerar visualizações
def gerar_visualizacoes(qtd):
    visualizacoes = []
    for i in range(501, 501 + qtd):
        id_visualizacao = f'{i:03}'
        id_perfil = random.choice(ids_perfis)
        dias_atras = random.randint(0, 365)
        visu_data = (datetime.today() - timedelta(days=dias_atras)).strftime('%Y-%m-%d')
        progresso = f'{random.randint(0,23):02}:{random.randint(0,59):02}:{random.randint(0,59):02}'
        visualizacoes.append((visu_data, progresso, id_visualizacao, id_perfil))
    return visualizacoes

# Gerar os dados
visualizacoes = gerar_visualizacoes(499)

# Inserir no banco
with conn.cursor() as cur:
    cur.executemany("""
        INSERT INTO Visualizacao (VisuData, Progresso, IDVisualizacao, IDPerfil)
        VALUES (%s, %s, %s, %s)
    """, visualizacoes)
    conn.commit()

conn.close()
print("Visualizações inseridas com sucesso!")

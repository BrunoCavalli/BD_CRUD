import psycopg2

# Configuração da conexão PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
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

def listar_tabelas():
    def listar_usuarios():
        cur.execute("SELECT IDUsuario, UserName, Email FROM Usuario ORDER BY IDUsuario")
        usuarios = cur.fetchall()
        if usuarios:
            print("\nLista de Usuários:")
            for u in usuarios:
                print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")
        else:
            print("\nNenhum usuário encontrado.")

    def listar_planos():
        cur.execute("SELECT idplano, planame, plapreco, telasimult, resolucaomax FROM plano ORDER BY idplano")
        planos = cur.fetchall()
        if planos:
            print("\nLista de Planos:")
            for p in planos:
                print(f"ID: {p[0]} | Nome: {p[1]} | Preço: {p[2]} | Telas Simultâneas: {p[3]} | Resolução Máxima: {p[4]}")
        else:
            print("\nNenhum plano encontrado.")

    def listar_titulos():
        cur.execute("SELECT idtitulo, titname, sinopse, anoestreia FROM titulo ORDER BY idtitulo")
        titulos = cur.fetchall()
        if titulos:
            print("\nLista de Títulos:")
            for t in titulos:
                print(f"ID: {t[0]} | Nome: {t[1]} | Sinopse: {t[2]} | Ano de Estreia: {t[3]}")
        else:
            print("\nNenhum título encontrado.")

    while True:
        print("\nEscolha a tabela para listar:")
        print("1 - Usuários")
        print("2 - Planos")
        print("3 - Títulos")
        print("4 - Voltar ao menu principal")

        escolha = input("Opção: ")

        if escolha == "1":
            listar_usuarios()
        elif escolha == "2":
            listar_planos()
        elif escolha == "3":
            listar_titulos()
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_usuario():
    id_usuario = input("IDUsuario: ")
    nome = input("Nome: ")
    data_nasc = input("Data Nasc (YYYY-MM-DD): ")
    email = input("Email: ")
    senha = input("Senha: ")
    id_plano = input("IDPlanoAssinado: ")

    try:
        cur.execute("""
            INSERT INTO Usuario (IDUsuario, UserName, DataNasc, Email, Senha, IDPlanoAssinado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_usuario, nome, data_nasc, email, senha, id_plano))
        conn.commit()
        print("Usuário adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar usuário: {e}")

def atualizar_usuario():
    id_usuario = input("Digite o IDUsuario do usuário para atualizar: ")
    nome = input("Novo Nome: ")
    data_nasc = input("Nova Data Nasc (YYYY-MM-DD): ")
    email = input("Novo Email: ")
    senha = input("Nova Senha: ")
    id_plano = input("Novo IDPlanoAssinado: ")

    try:
        cur.execute("""
            UPDATE Usuario SET UserName=%s, DataNasc=%s, Email=%s, Senha=%s, IDPlanoAssinado=%s
            WHERE IDUsuario=%s
        """, (nome, data_nasc, email, senha, id_plano, id_usuario))
        conn.commit()
        if cur.rowcount == 0:
            print("Usuário não encontrado.")
        else:
            print("Usuário atualizado com sucesso.")
    except Exception as e:
        print(f"Erro ao atualizar usuário: {e}")

def deletar_usuario():
    id_usuario = input("Digite o IDUsuario do usuário para deletar: ")
    try:
        cur.execute("DELETE FROM Usuario WHERE IDUsuario = %s", (id_usuario,))
        conn.commit()
        if cur.rowcount == 0:
            print("Usuário não encontrado.")
        else:
            print("Usuário deletado com sucesso.")
    except Exception as e:
        print(f"Erro ao deletar usuário: {e}")

def menu():
    while True:
        print("\n--- Menu CRUD ---")
        print("1 - Listar Tabelas")
        print("2 - Adicionar usuário")
        print("3 - Atualizar usuário")
        print("4 - Deletar usuário")
        print("5 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            listar_tabelas()
        elif escolha == "2":
            adicionar_usuario()
        elif escolha == "3":
            atualizar_usuario()
        elif escolha == "4":
            deletar_usuario()
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    menu()
    cur.close()
    conn.close()

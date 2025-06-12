import psycopg2
import sys
from datetime import datetime
import re

def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="bruno.cavalli"
        )
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
    sys.exit(1)

def detalhar_filme(id_titulo_filme):
    try:
        cur.execute("""
            SELECT T.TitName, T.Sinopse, T.AnoEstreia, F.Duracao
            FROM Titulo T
            JOIN Filme F ON T.IDTitulo = F.IDTitulo
            WHERE T.IDTitulo = %s
        """, (id_titulo_filme,))
        filme = cur.fetchone()
        if filme:
            print("\n--- Detalhes do Filme ---")
            print(f"Nome: {filme[0]}")
            print(f"Sinopse: {filme[1]}")
            print(f"Ano de Estreia: {filme[2]}")
            print(f"Duração: {filme[3]} min")
        else:
            print(f"Filme com ID {id_titulo_filme} não encontrado.")
    except Exception as e:
        print(f"Erro ao detalhar filme: {e}")

def listar_episodios(id_titulo_serie, num_temp):
    try:
        cur.execute("""
            SELECT EpName, NumEp, EpDuracao
            FROM Episodio
            WHERE IDTitulo = %s AND NumTemp = %s
            ORDER BY NumEp
        """, (id_titulo_serie, num_temp))
        episodios = cur.fetchall()
        if episodios:
            print(f"\n--- Episódios da Temporada {num_temp} ---")
            for ep in episodios:
                print(f"  {ep[1]}. {ep[0]} (Duração: {ep[2]} min)")
        else:
            print(f"Nenhum episódio encontrado para a Temporada {num_temp} da Série {id_titulo_serie}.")
    except Exception as e:
        print(f"Erro ao listar episódios: {e}")

def listar_temporadas(id_titulo_serie):
    try:
        cur.execute("""
            SELECT NumTemp, TempName
            FROM Temporada
            WHERE IDTitulo = %s
            ORDER BY NumTemp
        """, (id_titulo_serie,))
        temporadas = cur.fetchall()
        if temporadas:
            print(f"\n--- Temporadas da Série (ID: {id_titulo_serie}) ---")
            for t in temporadas:
                print(f"{t[0]}. {t[1]}")

            while True:
                escolha_temp = input("Digite o número da temporada para ver os episódios (ou 'v' para voltar): ").strip().lower()
                if escolha_temp == 'v':
                    break

                try:
                    num_temp_selecionada = int(escolha_temp)
                    numeros_temporadas_existentes = {t[0] for t in temporadas}
                    if num_temp_selecionada in numeros_temporadas_existentes:
                        listar_episodios(id_titulo_serie, num_temp_selecionada)
                    else:
                        print("Número de temporada inválido. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número ou 'v' para voltar.")
        else:
            print(f"Nenhuma temporada encontrada para a Série (ID: {id_titulo_serie}).")
    except Exception as e:
        print(f"Erro ao listar temporadas: {e}")

def listar_usuarios():
    try:
        cur.execute("SELECT IDUsuario, UserName, Email FROM Usuario ORDER BY IDUsuario")
        usuarios = cur.fetchall()
        if usuarios:
            print("\n--- Lista de Usuários ---")
            for u in usuarios:
                print(f"ID: {u[0]} | Nome: {u[1]} | Email: {u[2]}")
        else:
            print("\nNenhum usuário encontrado.")
    except Exception as e:
        print(f"Erro ao listar usuários: {e}")

def listar_planos():
    try:
        cur.execute("SELECT idplano, planame, plapreco, telasimult, resolucaomax FROM plano ORDER BY idplano")
        planos = cur.fetchall()
        if planos:
            print("\n--- Lista de Planos ---")
            for p in planos:
                print(f"ID: {p[0]} | Nome: {p[1]} | Preço: R${p[2]:.2f} | Telas Simultâneas: {p[3]} | Resolução Máxima: {p[4]}")
        else:
            print("\nNenhum plano encontrado.")
    except Exception as e:
        print(f"Erro ao listar planos: {e}")

def listar_filmes():
    try:
        cur.execute("SELECT T.IDTitulo, T.TitName FROM Titulo T JOIN Filme F ON T.IDTitulo = F.IDTitulo ORDER BY T.TitName")
        filmes = cur.fetchall()
        if filmes:
            print("\n--- Lista de Filmes ---")
            for f in filmes:
                print(f"ID: {f[0]} | Nome: {f[1]}")

            while True:
                escolha_filme_id = input("Digite o ID do filme para ver detalhes (ou 'v' para voltar): ").strip().lower()
                if escolha_filme_id == 'v':
                    break

                ids_filmes_existentes = {f[0] for f in filmes}
                if escolha_filme_id in ids_filmes_existentes:
                    detalhar_filme(escolha_filme_id)
                else:
                    print("ID de filme inválido. Tente novamente.")
        else:
            print("\nNenhum filme encontrado.")
    except Exception as e:
        print(f"Erro ao listar filmes: {e}")

def listar_series():
    try:
        cur.execute("SELECT T.IDTitulo, T.TitName FROM Titulo T JOIN Serie S ON T.IDTitulo = S.IDTitulo ORDER BY T.TitName")
        series = cur.fetchall()
        if series:
            print("\n--- Lista de Séries ---")
            for s in series:
                print(f"ID: {s[0]} | Nome: {s[1]}")

            while True:
                escolha_serie_id = input("Digite o ID da série para ver as temporadas (ou 'v' para voltar): ").strip().lower()
                if escolha_serie_id == 'v':
                    break

                ids_series_existentes = {s[0] for s in series}
                if escolha_serie_id in ids_series_existentes:
                    listar_temporadas(escolha_serie_id)
                else:
                    print("ID de série inválido. Tente novamente.")
        else:
            print("\nNenhuma série encontrada.")
    except Exception as e:
        print(f"Erro ao listar séries: {e}")

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
            menu_listar_informacoes()
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

def menu_listar_informacoes():
    while True:
        print("\n--- Listar Informações ---")
        print("1 - Usuários")
        print("2 - Planos")
        print("3 - Filmes")
        print("4 - Séries")
        print("5 - Voltar ao menu principal")

        escolha = input("Escolha a tabela para listar: ")

        if escolha == "1":
            listar_usuarios()
        elif escolha == "2":
            listar_planos()
        elif escolha == "3":
            listar_filmes()
        elif escolha == "4":
            listar_series()
        elif escolha == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

def adicionar_usuario():
    while True:
        id_usuario = input("IDUsuario (exatamente 3 caracteres): ").strip()
        if len(id_usuario) == 3:
            break
        else:
            print("Erro: IDUsuario deve ter exatamente 3 caracteres. Tente novamente.")

    nome = input("Nome: ").strip()
    if not nome:
        print("Erro: Nome não pode ser vazio.")
        return

    while True:
        data_nasc_str = input("Data Nasc (YYYY-MM-DD): ").strip()
        try:
            data_nasc = datetime.strptime(data_nasc_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Erro: Formato de data inválido ou data irreal. Use YYYY-MM-DD. Tente novamente.")

    while True:
        email = input("Email: ").strip()
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            break
        else:
            print("Erro: Formato de e-mail inválido. Tente novamente.")

    senha = input("Senha: ").strip()
    if not senha:
        print("Erro: Senha não pode ser vazia.")
        return

    while True:
        id_plano = input("IDPlanoAssinado (exatamente 3 caracteres): ").strip()
        if len(id_plano) == 3:
            break
        else:
            print("Erro: IDPlanoAssinado deve ter exatamente 3 caracteres. Tente novamente.")

    try:
        cur.execute("""
            INSERT INTO Usuario (IDUsuario, UserName, DataNasc, Email, Senha, IDPlanoAssinado)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (id_usuario, nome, data_nasc, email, senha, id_plano))
        conn.commit()
        print("Usuário adicionado com sucesso.")
    except psycopg2.IntegrityError as e:
        conn.rollback()
        if "unique_email_key" in str(e):
            print(f"Erro: Este e-mail já está em uso. Por favor, use outro e-mail.")
        elif "usuario_idplanoassinado_fkey" in str(e):
             print(f"Erro: O IDPlanoAssinado '{id_plano}' não existe na tabela de Planos.")
        elif "usuario_pkey" in str(e):
             print(f"Erro: O IDUsuario '{id_usuario}' já existe. Por favor, use outro ID.")
        else:
            print(f"Erro de integridade do banco de dados: {e}")
    except Exception as e:
        conn.rollback()
        print(f"Erro inesperado ao adicionar usuário: {e}")

def atualizar_usuario():
    while True:
        id_usuario = input("Digite o IDUsuario do usuário para atualizar (exatamente 3 caracteres): ").strip()
        if len(id_usuario) == 3:
            cur.execute("SELECT UserName, DataNasc, Email, Senha, IDPlanoAssinado FROM Usuario WHERE IDUsuario = %s", (id_usuario,))
            dados_atuais = cur.fetchone()
            if dados_atuais:
                break
            else:
                print(f"Erro: Usuário com ID '{id_usuario}' não encontrado. Tente novamente.")
        else:
            print("Erro: IDUsuario deve ter exatamente 3 caracteres. Tente novamente.")

    print("\n--- Digite os novos dados (deixe em branco para manter o atual) ---")

    current_username, current_datanasc, current_email, current_senha, current_idplano = dados_atuais

    nome_novo = input(f"Novo Nome (atual: {current_username}): ").strip()
    nome = nome_novo if nome_novo else current_username

    while True:
        data_nasc_str_novo = input(f"Nova Data Nasc (YYYY-MM-DD, atual: {current_datanasc}): ").strip()
        if not data_nasc_str_novo:
            data_nasc = current_datanasc
            break
        try:
            data_nasc = datetime.strptime(data_nasc_str_novo, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Erro: Formato de data inválido ou data irreal. Use YYYY-MM-DD. Tente novamente.")

    while True:
        email_novo = input(f"Novo Email (atual: {current_email}): ").strip()
        if not email_novo:
            email = current_email
            break
        if re.match(r"[^@]+@[^@]+\.[^@]+", email_novo):
            email = email_novo
            break
        else:
            print("Erro: Formato de e-mail inválido. Tente novamente.")

    senha_nova = input(f"Nova Senha (atual: {current_senha}): ").strip()
    senha = senha_nova if senha_nova else current_senha

    while True:
        id_plano_novo_str = input(f"Novo IDPlanoAssinado (exatamente 3 caracteres, atual: {current_idplano}): ").strip()
        if not id_plano_novo_str:
            id_plano = current_idplano
            break
        if len(id_plano_novo_str) == 3:
            id_plano = id_plano_novo_str
            break
        else:
            print("Erro: IDPlanoAssinado deve ter exatamente 3 caracteres. Tente novamente.")

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
    except psycopg2.IntegrityError as e:
        conn.rollback()
        if "unique_email_key" in str(e):
            print(f"Erro: Este e-mail já está em uso por outro usuário. Por favor, use outro e-mail.")
        elif "usuario_idplanoassinado_fkey" in str(e):
             print(f"Erro: O IDPlanoAssinado '{id_plano}' não existe na tabela de Planos.")
        else:
            print(f"Erro de integridade do banco de dados: {e}")
    except Exception as e:
        conn.rollback()
        print(f"Erro inesperado ao atualizar usuário: {e}")

def deletar_usuario():
    id_usuario = input("Digite o IDUsuario do usuário para deletar: ").strip()

    conn.autocommit = False

    try:
        cur.execute("SELECT IDPerfil FROM Perfil WHERE IDUsuario = %s", (id_usuario,))
        ids_perfis = [row[0] for row in cur.fetchall()]

        if not ids_perfis:
            print(f"Usuário com ID {id_usuario} não encontrado ou não possui perfis.")
            conn.autocommit = True
            return

        cur.execute("""
            SELECT IDVisualizacao FROM Visualizacao WHERE IDPerfil = ANY(%s)
        """, (ids_perfis,))
        ids_visualizacoes = [row[0] for row in cur.fetchall()]

        if ids_visualizacoes:
            cur.execute("DELETE FROM VisEpisodio WHERE IDVisualizacao = ANY(%s)", (ids_visualizacoes,))
            print(f"  - {cur.rowcount} registros em VisEpisodio deletados.")

            cur.execute("DELETE FROM VisFilme WHERE IDVisualizacao = ANY(%s)", (ids_visualizacoes,))
            print(f"  - {cur.rowcount} registros em VisFilme deletados.")

        cur.execute("DELETE FROM Visualizacao WHERE IDPerfil = ANY(%s)", (ids_perfis,))
        print(f"  - {cur.rowcount} registros em Visualizacao deletados.")

        cur.execute("DELETE FROM Perfil WHERE IDUsuario = %s", (id_usuario,))
        print(f"  - {cur.rowcount} registros em Perfil deletados.")

        cur.execute("DELETE FROM Usuario WHERE IDUsuario = %s", (id_usuario,))
        if cur.rowcount == 0:
            print("Usuário não encontrado (após tentar deletar dependências).")
            conn.rollback()
        else:
            print(f"Usuário {id_usuario} deletado com sucesso.")
            conn.commit()

    except Exception as e:
        conn.rollback()
        print(f"Erro ao deletar usuário e suas dependências: {e}")
    finally:
        conn.autocommit = True

# Início do programa
if __name__ == "__main__":
    menu()
    if cur:
        cur.close()
    if conn:
        conn.close()

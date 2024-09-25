import mysql.connector
from conexao import conn

# TODO: Fazer a verificação de email e CPF cadastrado, e criar as outras funções

# função que pega os dados da interface e joga na funcao criar usuario
def enviar_dados(nome, email, senha):
    criar_usuario(nome, email, senha)


def criar_usuario(nome, email, senha):

    try:
        if conn.is_connected():
            print('Banco conectado com sucesso!')

            cursor = conn.cursor()

            sql = 'INSERT INTO USUARIO (nome, email, senha) VALUES (%s, %s, %s)'
            values = (nome, email, senha)

            cursor.execute(sql, values)
            conn.commit()
            print('Usuário cadastrado com sucesso!')
          
        else:
            print('Falha ao conectar com o banco!')

    except mysql.connector.Error as err:
        print(f'Erro: {err}')

    finally:
        if cursor is not None:
            cursor.close()

def listar_usuario():
    try:
        if conn.is_connected():
            print('Banco de dados conectado com sucesso!!')

            cursor = conn.cursor()

            cursor.execute('SELECT ID, NOME, EMAIL FROM USUARIO;')

            usuarios = cursor.fetchall()
            return usuarios


    except mysql.connector.Error as e:
        print(f'Erro: {e}')

    finally:
        if cursor:
            cursor.close()


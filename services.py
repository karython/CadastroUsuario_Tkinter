from conexao import *

def autenticacao(login, senha):
    cursor = None
    try:
        if conn.is_connected():
            cursor = conn.cursor()

            sql = 'select email, senha from USUARIO where email = %s and senha = %s'
            values = (login, senha)

            cursor.execute(sql, values)

            result = cursor.fetchone()
            if result:
                return True
            else:
                return False
        
    except mysql.connector.Error as err:
        return f'Erro: {err}'
    finally:
        if cursor is not None:  # Verifique se cursor foi inicializado
            cursor.close()


def cadastrar_usuario(nome, email, senha):
    cursor = None
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            
            # verifica se o usuario já existe
            cursor.execute('select email from USUARIO where email = %s', (email,))
            resultado = cursor.fetchone()

            if resultado:
                return 'Já existe um usuário com esse email!'

            sql = 'insert into USUARIO (nome, email, senha) values (%s, %s, %s)'
            values = (nome, email, senha)

            cursor.execute(sql, values)
            conn.commit()

            return 'Usuário cadastrado com sucesso!'
            
                

    except mysql.connector.Error as err:
        return f'Erro: {err}'
    finally:
        if cursor is not None:  # Verifique se cursor foi inicializado
            cursor.close()

def listar_usuario():
    cursor = None
    try:
        if conn.is_connected:
            cursor = conn.cursor()
            
            cursor.execute('select * from vw_usuarios')

            result = cursor.fetchall()

            return result

    except mysql.connector.Error as err:
        return f'Erro: {err}'
    finally:
        if cursor is not None:  # Verifique se cursor foi inicializado
            cursor.close()


def remover_usuario(usuario_id):
    cursor = None
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            sql = 'delete from USUARIO where id = %s'
            values = (usuario_id,)

            cursor.execute(sql, values)
            conn.commit()
            return 'Usuário removido com sucesso!'

    except mysql.connector.Error as err:
        return f'Erro: {err}'
    finally:
        if cursor is not None:
            cursor.close()
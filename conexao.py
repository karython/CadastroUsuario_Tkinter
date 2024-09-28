import mysql
import mysql.connector

conn = mysql.connector.connect(
    host = 'srv1061.hstgr.io',
    user = 'u275872813_karython',
    password = '@Karython0705',
    database = 'u275872813_CRUD'
)
    

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
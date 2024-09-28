from flask import Flask, redirect, render_template, request, url_for, flash, session
from services import autenticacao, listar_usuario, remover_usuario, cadastrar_usuario

app = Flask(__name__)
app.secret_key = 'sistemaSGU'

@app.route('/')
def index():
    return render_template('login.html')

# verificacao no banco se o usuario existe
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # limpar a sessao antes de iniciar outra
        session.pop('_flashes', None)
        login = request.form['login']
        senha = request.form['password']

        if autenticacao(login, senha):
            session['usuario_logado'] = True
            return redirect(url_for('home'))
        else:
            flash('Usuario ou senha invalidos.')
            return redirect(url_for('index'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    if not session.get('usuario_logado'):
        flash('Você precisa fazer login primeiro.')
        return redirect(url_for('index'))
    usuarios = None
    if request.method == 'GET':
        usuarios = listar_usuario()
    return render_template('home.html', usuarios=usuarios)

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    session.pop('usuario_logado', None) # remover o estado de login da sessão
    flash('Você foi desconectado.')
    return redirect(url_for('index'))


@app.route('/remover/<int:id>', methods=['POST'])
def remover_usuario_route(id):
    resultado = remover_usuario(id)
    flash(resultado)
    return redirect(url_for('home'))

@app.route('/cadastrar', methods=['POST'])
# os dados estao vindo via request entao a função nao precisa de parametros
def cadastrar_usuario_route():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        resultado = cadastrar_usuario(nome, email, senha)
        flash(resultado)
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
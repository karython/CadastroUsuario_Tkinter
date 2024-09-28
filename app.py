from flask import Flask, redirect, render_template, request, url_for, flash, session
from conexao import autenticacao, listar_usuario

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

if __name__ == '__main__':
    app.run(debug=True)
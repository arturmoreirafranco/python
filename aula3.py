from flask import Flask, render_template


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def index():
    return render_template('curriculo.html') # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/cotemig/<nome>') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def exibir_nome(nome):
    return f'Nome: {nome}'

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento

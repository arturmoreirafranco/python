from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/decorator') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Um decorator em Python é como uma "etiqueta inteligente" que você coloca em cima de uma função para dar a ela novos comportamentos sem precisar reescrever o código dela. Ele serve para reaproveitar lógicas comuns — como segurança, logs ou cronometragem — de forma limpa e organizada.No Flask, o exemplo @app.route("/") funciona como um direcionador: ele avisa ao servidor que aquela função específica deve ser executada sempre que alguém acessar um endereço determinado no navegador. Em resumo, o decorator "embrulha" a sua função e adiciona uma funcionalidade extra (como transformá-la em uma página de internet) de maneira automática.' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento

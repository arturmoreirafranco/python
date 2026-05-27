from flask import Flask, render_template, request
from calculadora import calcular


app = Flask(__name__)

@app.route('/', methods=['POST'])
def calculador():
        return calcular()
    
@app.route('/')
def index():
    return render_template('calculadora.html', etapas='', resultado='' )

if __name__ == "__main__":
    app.run(debug=True)

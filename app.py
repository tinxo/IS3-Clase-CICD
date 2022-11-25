from crypt import methods
from flask import Flask, render_template, request
import functions.calculadora as calc

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/form")
def form():
    return render_template('form.html')

@app.route("/result", methods=['POST'])
def result():
    # linea de ejemplo para hacer un commit
    # Se tienen que obtener los valores ingresados en el form
    num_1 = request.form.get("num_1", type=int)
    num_2 = request.form.get("num_2", type=int)
    operador = request.form.get("operador", type=str)
    operaciones = {
        'Suma' : calc.suma,
    }
    fx = operaciones.get(operador.split(" ")[0].strip())
    resultado = fx(num_1, num_2)
    return render_template('result.html', res=resultado)
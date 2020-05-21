from flask import Flask
from flask import render_template, session
from CBanda import Banda
import random

b = Banda()
b.AsignarInst()

app = Flask(__name__)
app.secret_key = 'unaClave'

@app.route('/')
def index():
    b.musico.clear()
    session['band'] = b.AsignarInst()
    return render_template('index.html')

@app.route('/preparar')
def preparar():
    return render_template('preparar.html', lista = b.musico)

@app.route('/tocar')
def tocar():
    return render_template('tocar.html', lista = b.musico)

if __name__ == '__main__':
    app.run()


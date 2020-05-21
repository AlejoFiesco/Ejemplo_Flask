from flask import Flask
from flask import render_template
from CBanda import Banda
import random

cm = random.randint(5, 10)
b = Banda(cm)
b.AsignarInst()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/preparar')
def preparar():
    return render_template('preparar.html', lista = b.musico)

if __name__ == '__main__':
    app.run()


from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

preguntas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/retos')
def retos():
    return render_template('retos.html')

@app.route('/preguntas_respuestas', methods=['GET', 'POST'])
def preguntas_respuestas():
    if request.method == 'POST':
        pregunta = request.form['pregunta']
        preguntas.append({'pregunta': pregunta, 'respuestas': []})
        return redirect(url_for('preguntas_respuestas'))
    return render_template('preguntas_respuestas.html', preguntas=preguntas, enumerate=enumerate)

@app.route('/responder/<int:pregunta_id>', methods=['POST'])
def responder(pregunta_id):
    respuesta = request.form['respuesta']
    preguntas[pregunta_id]['respuestas'].append(respuesta)
    return redirect(url_for('preguntas_respuestas'))

@app.route('/recursos')
def recursos():
    return render_template('recursos.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Manejar logica de inicio de sesion aqui
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Manejar logica de registro aqui
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
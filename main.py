from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def command():
    if request.method == 'POST':       
        if request.form.get("boton") == "adelante":
            print("adelante")
        elif request.form.get("boton") == "atras":
            print("atras")
        elif request.form.get("boton") == "izquierda":
            print("izquierda")
        elif request.form.get("boton") == "derecha":
            print("derecha")
        elif request.form.get("boton") == "alto":
            print("alto")
        else:
            print("Comando incorrecto!")
            print(request.form.get("boton"))
    return "OK"        

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
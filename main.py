from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/robot.html")
def robot():
    return render_template('robot.html')

@app.route("/manual.html")
def manual():
    return render_template('manual.html')

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

@app.route('/robot', methods=['POST'])
def commandrobot():
    if request.method == 'POST':       
        if request.form.get("boton2") == "abrir":
            print("abrir")
        elif request.form.get("boton2") == "cerrar":
            print("cerrar")
        else:
            print("Comando incorrecto!")
            print(request.form.get("boton2"))
    return "OK"   

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

from flask import Flask, render_template, request
import serial
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)  # open serial port Windows

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

@app.errorhandler(404)
def page_not_found(e):
    # Tenemos en cuenta que establecemos el estado explicito de 404
    return render_template('error.html'), 404

@app.route('/control', methods=['POST'])
def command():
    if request.method == 'POST':       
        if request.form.get("boton") == "adelante":
            print("adelante")
            ser.write(b'f \n')     # write a string
        elif request.form.get("boton") == "atras":
            print("atras")
            ser.write(b'b \n')     # write a string
        elif request.form.get("boton") == "izquierda":
            print("izquierda")
            ser.write(b'l \n')     # write a string
        elif request.form.get("boton") == "derecha":
            print("derecha")
            ser.write(b'r \n')     # write a string
        elif request.form.get("boton") == "alto":
            print("alto")
            ser.write(b's \n')     # write a string
        else:   
            print("Comando incorrecto!")
            print(request.form.get("boton"))
    return "OK"        

@app.route('/robot', methods=['POST'])
def commandrobot():
    if request.method == 'POST':       
        if request.form.get("boton2") == "abrir":
            print("abrir")
            ser.write(b'abrir \n')     # write a string
        elif request.form.get("boton2") == "cerrar":
            print("cerrar")
            ser.write(b'cerrar \n')     # write a string
        else:
            print("Comando incorrecto!")
            print(request.form.get("boton2"))
    return "OK"   

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)


#127.0.0.1 (ip home)
#172.16.0.114 (raspy)
#id: pi
#password: raspberry
#cd robotto/
#git pull origin master (actualizar)
#ls 

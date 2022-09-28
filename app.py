from flask import Flask, render_template
app=Flask(__name__)

@app.route('/Solicitud')
def Solicitud():
    
    return render_template("SolicitudContraseña.html") # nombre es la variable de la funcion home() y nombre1 es la variable del documento html, en caso el de index.html

@app.route('/Recuperacion')
def Recuperacion():
    
    return render_template("Recuperacion.html") # nombre es la variable de la funcion home() y nombre1 es la variable del documento html, en caso el de index.html



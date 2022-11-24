from flask import Flask, render_template, request

#Instancia de Flask. aplicación

app = Flask(__name__)

# Creamos nuestro primer route "/login"
@app.route("/")
def template():
    #Renderizamos la plantilla Formulario HTML
    return render_template("form.html")

# Definimos el route con un POST

@app.route("/usuario", methods=["POST"])
def usuarios():
    #Obtenemos los parámetros de la info de "nombreUser"
    #Esto lo hacemos con el diccionario "form"
    nombreUser = request.form("nombreUser")

    #Retornamos la respuesta
    return "<h1>Bienvenido " + nombreUser + "</h1>"


    if __name__ == "__main__":
        #Iniciamos la app en modo debug
        app.run(debug=True)
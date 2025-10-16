from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route("/")
def lobby():
    return render_template("lobby.html")

@app.route("/inicio")
def inicio():
    return render_template("inicio.html")

@app.route("/animales")
def animales():
    return render_template("animales.html")

@app.route("/maravillas")
def maravillas():
    return render_template("maravillas.html")

@app.route("/vehiculos")
def vehiculos():
    return render_template("vehiculos.html")

@app.route("/acerca")
def acerca():
    return render_template("acerca.html")

@app.route("/formulario")
def formulario():
    return render_template("formulario.html")


@app.route("/registro", methods=["POST"])
def registro():
    error = None
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        correo = request.form.get("correo")
        genero = request.form.get("genero")
        contraseña=request.form.get("contraseña")
        dia = request.form.get("dia")
        mes = request.form.get("mes")
        año = request.form.get("año")
        return redirect(url_for("inicio"))
    return render_template("formulario.html")


if __name__ == "__main__":
    app.run(debug=True)

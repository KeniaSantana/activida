from flask import Flask, render_template, request, redirect, url_for, flash, session


app = Flask(__name__)
app.secret_key = "clave_secreta" 


usuarios = {}

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
    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    correo = request.form.get("correo")
    genero = request.form.get("genero")
    contraseña = request.form.get("contraseña")
    dia = request.form.get("dia")
    mes = request.form.get("mes")
    año = request.form.get("año")

    if correo in usuarios:
        flash("Este correo ya está registrado.", "warning")
        return redirect(url_for("formulario"))
    else:
        usuarios[correo] = contraseña
        flash("Registro exitoso. Ahora puedes iniciar sesión.", "success")
        return redirect(url_for("sesion"))


@app.route("/sesion")
def sesion():
    return render_template("sesion.html")




@app.route("/iniciar", methods=["POST"])
def iniciar():
    email = request.form.get("email")
    password = request.form.get("password")
    if email not in usuarios:
        flash("El correo no está registrado.", "danger")
        return redirect(url_for("sesion"))
    elif usuarios[email] != password:
        flash("La contraseña no coincide.", "danger")
        return redirect(url_for("sesion"))
    else:
        # Guardamos el usuario en la sesión
        session["usuario"] = email
        session["logout"] = True
        flash(f"Inicio de sesión exitoso. Bienvenido, {email}!", "success")
        return redirect(url_for("inicio"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "info")
    return redirect(url_for("inicio"))



if __name__ == "__main__":
    app.run(debug=True)

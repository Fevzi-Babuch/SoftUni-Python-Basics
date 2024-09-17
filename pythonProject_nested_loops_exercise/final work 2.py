from flask_ngrok import run_with_ngrok
from flask import Flask, render_template, url_for, request, redirect
import json
import os
from types import SimpleNamespace

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run

usuarios = []


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        email = request.form.get("email")
        nombre = request.form.get("nombre")
        apellido = request.form.get("apellido")
        contraseña = request.form.get("contraseña")
        telefono = request.form.get("telefono")
        edad = request.form.get("edad")
        usuarios.append(
            {"Email": email, "Nombre": nombre, "Apellidos": apellido, "Contraseña": contraseña, "Telefono": telefono,
             "Edad": edad})
        with open('usuarios.json', 'w') as f:
            json.dump(usuarios, f)
        return redirect("/")
    return render_template("index.html")


@app.route("/list")
def list_users():
    with open('usuarios.json') as f:
        users = json.load(f, object_hook=lambda d: SimpleNamespace(**d))
    return render_template("list.html", users=users)


@app.route("/delete", methods=["GET"])
def delete_user():
    email = request.args.get("email")
    with open('usuarios.json') as f:
        users = json.load(f)
    users = [user for user in users if user.get("Email") != email]
    with open('usuarios.json', 'w') as f:
        json.dump(users, f)
    return redirect("/list")


@app.route("/edit", methods=["GET", "POST"])
def edit_user():
    email = request.args.get("email")
    with open('usuarios.json') as f:
        users = json.load(f)
    user = [user for user in users if user.get("Email") == email][0]
    if request.method == "POST":
        user["Nombre"] = request.form.get("nombre")
        user["Apellidos"] = request.form.get("apellido")
        user["Contraseña"] = request.form.get("contraseña")
        user["Telefono"] = request.form.get("telefono")
        user["Edad"] = request.form.get("edad")
        users = [user if user.get("Email") != email else user for user in users]
        with open('usuarios.json', 'w') as f:
            json.dump(users, f)
        return redirect("/list")
    return render_template("edit.html", user=user)


if __name__ == "__main__":
    if not os.path.exists('usuarios.json'):
        with open('usuarios.json', 'w') as f:
            json.dump([], f)
    app.run()
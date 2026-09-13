from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import conectar

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.secret_key = "financeweb2026"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form.get("nome")
        email = request.form.get("email")
        telefone = request.form.get("telefone")
        senha = request.form.get("senha")
        confirmar_senha = request.form.get("confirmar_senha")

        if senha != confirmar_senha:

            flash("As senhas não coincidem.", "erro")
            return redirect(url_for("cadastro"))

        try:

            con = conectar()
            cursor = con.cursor()

            cursor.execute(
                """
                INSERT INTO usuarios
                (
                    nome,
                    email,
                    telefone_whatsapp,
                    senha
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    nome,
                    email,
                    telefone,
                    senha
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash("Usuário cadastrado com sucesso!", "sucesso")
            return redirect(url_for("cadastro"))

        except Exception as erro:

            print("Erro:", erro)

            flash("Erro ao cadastrar usuário.", "erro")
            return redirect(url_for("cadastro"))

    return render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        senha = request.form.get("senha")

        try:

            con = conectar()
            cursor = con.cursor()

            cursor.execute(
            """
            select * from usuarios where email = %s and senha = %s
            """,
            (
                email,
                senha
            )
            )
            usuario = cursor.fetchone()

            cursor.close()
            con.close()

            if usuario:
                session["usuario_id"] = usuario[0]
                session["usuario_nome"] = usuario[1]
                session["usuario_email"] = usuario[2]
                flash("Login realizado com sucesso!", "sucesso")
                return redirect(url_for("dashboard"))
            else:
                flash("E-mail ou senha incorretos.", "erro")

            return redirect(url_for("login"))

        except Exception as erro:

            print("Erro:", erro)

            flash("Erro ao realizar login.", "erro")

            return redirect(url_for("login"))    

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar o dashboard.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    return render_template(
        "dashboard.html"
    )

try:

    con = conectar()

    print("✅ Conectado ao PostgreSQL com sucesso!")

    con.close()

except Exception as erro:

    print("❌ Erro ao conectar:", erro)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

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

@app.route("/usuarios")
def usuarios():
    if "usuario_id" not in session:

        flash(
            "Faça login para acessar a lista de usuários.",
            "erro"
        )

        return redirect(
            url_for("dashboard")
        )

    if not session.get("usuario_admin"):

            flash(
                "Acesso restrito ao administrador.",
                "erro"
            )

            return redirect(
                url_for("dashboard")
           )
    
    try:

        con = conectar()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT id, nome, email, telefone_whatsapp,data_cadastro,ativo, administrador
            from usuarios
            order by id
            """
        )

        usuarios = cursor.fetchall()

        cursor.close()
        con.close()

        return render_template(
            "usuarios.html",
            usuarios=usuarios
        )
    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao buscar usuários.",
            "erro"
        )

        return redirect(
            url_for("home")
        )

@app.route("/toggle_admin/<int:id>")
def toggle_admin(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    if not session.get("usuario_admin"):

        flash(
            "Acesso restrito ao administrador.",
            "erro"
        )

        return redirect(
            url_for("dashboard")
        )

    try:

        # Impede que o usuário altere o próprio perfil
        if id == session.get("usuario_id"):

            flash(
                "Você não pode alterar seu próprio status de administrador.",
                "erro"
            )

            return redirect(
                url_for("usuarios")
            )

        con = conectar()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT administrador
            FROM usuarios
            WHERE id = %s
            """,
            (id,)
        )

        usuario = cursor.fetchone()

        if not usuario:

            flash(
                "Usuário não encontrado.",
                "erro"
            )

            cursor.close()
            con.close()

            return redirect(
                url_for("usuarios")
            )

        # Se o usuário é administrador,
        # verificar se é o último administrador do sistema
        if usuario[0]:  # Se for administrador
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM usuarios
                WHERE administrador = TRUE
                """
            )

            total_admins = cursor.fetchone()[0]

            if total_admins == 1:

                flash(
                    "Não é possível remover o último administrador do sistema.",
                    "erro"
                )

                cursor.close()
                con.close()

                return redirect(
                    url_for("usuarios")
                )

        # ESTA LINHA PRECISA FICAR FORA DO IF
        novo_status = not usuario[0]

        cursor.execute(
            """
            UPDATE usuarios
            SET administrador = %s
            WHERE id = %s
            """,
            (
                novo_status,
                id
            )
        )

        con.commit()

        cursor.close()
        con.close()

        flash(
            "Perfil administrativo atualizado com sucesso!",
            "sucesso"
        )

        return redirect(
            url_for("usuarios")
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao atualizar usuário.",
            "erro"
        )

        return redirect(
            url_for("usuarios")
        )

@app.route("/excluir_usuario/<int:id>")
def excluir_usuario(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    if not session.get("usuario_admin"):

        flash(
            "Acesso restrito ao administrador.",
            "erro"
        )

        return redirect(
            url_for("dashboard")
        )

    try:

        # Não permite excluir a própria conta

        if id == session.get("usuario_id"):

            flash(
                "Você não pode excluir sua própria conta.",
                "erro"
            )

            return redirect(
                url_for("usuarios")
            )

        con = conectar()
        cursor = con.cursor()

        # Busca o status administrativo do usuário

        cursor.execute(
            """
            SELECT administrador
            FROM usuarios
            WHERE id = %s
            """,
            (id,)
        )

        usuario = cursor.fetchone()

        if not usuario:

            flash(
                "Usuário não encontrado.",
                "erro"
            )

            cursor.close()
            con.close()

            return redirect(
                url_for("usuarios")
            )

        # Se for administrador, verifica se é o último

        if usuario[0]:  # Se for administrador
            cursor.execute(
                """
                SELECT COUNT(*)
                FROM usuarios
                WHERE administrador = TRUE
                """
            )

            total_admins = cursor.fetchone()[0]

            if total_admins == 1:

                flash(
                    "Não é possível excluir o último administrador do sistema.",
                    "erro"
                )

                cursor.close()
                con.close()

                return redirect(
                    url_for("usuarios")
                )

        # Exclusão

        cursor.execute(
            """
            DELETE FROM usuarios
            WHERE id = %s
            """,
            (id,)
        )

        con.commit()

        cursor.close()
        con.close()

        flash(
            "Usuário excluído com sucesso!",
            "sucesso"
        )

        return redirect(
            url_for("usuarios")
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao excluir usuário.",
            "erro"
        )

        return redirect(
            url_for("usuarios")
        )

@app.route("/toggle_usuario/<int:id>")
def toggle_usuario(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    if not session.get("usuario_admin"):

        flash(
            "Acesso restrito ao administrador.",
            "erro"
        )

        return redirect(
            url_for("dashboard")
        )

    try:

        con = conectar()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT ativo
            FROM usuarios
            WHERE id = %s
            """,
            (id,)
        )

        usuario = cursor.fetchone()

        if not usuario:

            flash(
                "Usuário não encontrado.",
                "erro"
            )

            return redirect(
                url_for("usuarios")
            )

        novo_status = not usuario[0]

        cursor.execute(
            """
            UPDATE usuarios
            SET ativo = %s
            WHERE id = %s
            """,
            (
                novo_status,
                id
            )
        )

        con.commit()

        cursor.close()
        con.close()

        flash(
            "Status do usuário atualizado com sucesso!",
            "sucesso"
        )

        return redirect(
            url_for("usuarios")
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao atualizar usuário.",
            "erro"
        )

        return redirect(
            url_for("usuarios")
        )

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
            SELECT
            id,
            nome,
            email,
            telefone_whatsapp,
            senha,
            data_cadastro,
            ativo,
            administrador
            FROM usuarios
            WHERE email = %s
            AND senha = %s
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

                if not usuario[6]:  # Verifica se o usuário está ativo
                    flash("Usuário inativo. Entre em contato com o administrador.", "erro")
                    return redirect(url_for("login"))
                else:                
                    session["usuario_id"] = usuario[0]
                    session["usuario_nome"] = usuario[1]
                    session["usuario_email"] = usuario[2]
                    session["usuario_telefone"] = usuario[3]
                    session["usuario_senha"] = usuario[4]
                    session["usuario_data_cadastro"] = usuario[5]
                    session["usuario_ativo"] = usuario[6]
                    session["usuario_admin"] = usuario[7]
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

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "Logout realizado com sucesso!",
        "sucesso"
    )

    return redirect(
        url_for("home")
    )

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

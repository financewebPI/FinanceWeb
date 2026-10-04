from flask import Flask, render_template, request, redirect, url_for, flash, session
from database import conectar

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.secret_key = "financeweb2026"

# ------------------ Rotas ------------------ #

# ------------------ Rota Principal ------------------ #
@app.route("/")
def home():
    return render_template("index.html")

# ------------------ Rota de Usuários ------------------ #
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

# ------------------ Rota para Alterar Status de Administrador ------------------ #
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

        if usuario[0]: 
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

# ------------------ Rota para Excluir Usuário ------------------ #
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

        if usuario[0]:  
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

# ------------------ Rota para Alternar Status do Usuário ------------------ #
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

# ------------------ Rota de Cadastro ------------------ #
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

# ------------------ Rota de Login ------------------ #
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

# ------------------ Rota de Logout ------------------ #
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

# ------------------ Rota do Esqueci Senha ------------------ #
@app.route("/esqueci-senha", methods=["GET", "POST"])
def esqueci_senha():

    if request.method == "POST":

        email = request.form.get("email")

        try:

            con = conectar()
            cursor = con.cursor()

            cursor.execute(
                """
                SELECT id
                FROM usuarios
                WHERE email = %s
                """,
                (email,)
            )

            usuario = cursor.fetchone()

            cursor.close()
            con.close()

            if not usuario:

                flash(
                    "E-mail não encontrado.",
                    "erro"
                )

                return redirect(
                    url_for("esqueci_senha")
                )

            return redirect(
                url_for(
                    "redefinir_senha",
                    id=usuario[0]
                )
            )

        except Exception as erro:

            print("Erro:", erro)

            flash(
                "Erro ao processar recuperação de senha.",
                "erro"
            )

            return redirect(
                url_for("esqueci_senha")
            )

    return render_template(
        "esqueci_senha.html"
    )

# ------------------ Rota redefinir senha ------------------ #
@app.route(
    "/redefinir-senha/<int:id>",
    methods=["GET", "POST"]
)
def redefinir_senha(id):

    try:

        con = conectar()
        cursor = con.cursor()

        # Verifica se o usuário existe

        cursor.execute(
            """
            SELECT id
            FROM usuarios
            WHERE id = %s
            """,
            (
                id,
            )
        )

        usuario = cursor.fetchone()

        if not usuario:

            cursor.close()
            con.close()

            flash(
                "Usuário não encontrado.",
                "erro"
            )

            return redirect(
                url_for("esqueci_senha")
            )

        # ==================================
        # PROCESSAR NOVA SENHA
        # ==================================

        if request.method == "POST":

            senha = request.form.get("senha")
            confirmar_senha = request.form.get(
                "confirmar_senha"
            )

            if senha != confirmar_senha:

                flash(
                    "As senhas não coincidem.",
                    "erro"
                )

                cursor.close()
                con.close()

                return redirect(
                    url_for(
                        "redefinir_senha",
                        id=id
                    )
                )

            cursor.execute(
                """
                UPDATE usuarios
                SET senha = %s
                WHERE id = %s
                """,
                (
                    senha,
                    id
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash(
                "Senha redefinida com sucesso!",
                "sucesso"
            )

            return redirect(
                url_for("login")
            )

        cursor.close()
        con.close()

        return render_template(
            "redefinir_senha.html"
        )

    except Exception as erro:

        print(
            "Erro ao redefinir senha:",
            erro
        )

        flash(
            "Erro ao redefinir senha.",
            "erro"
        )

        return redirect(
            url_for("esqueci_senha")
        )
# ------------------ Rota do Dashboard ------------------ #
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

    try:

        con = conectar()
        cursor = con.cursor()

        # ==========================
        # TOTAL DE RECEITAS
        # ==========================

        cursor.execute(
            """
            SELECT COALESCE(SUM(valor), 0)
            FROM receitas
            WHERE usuario_id = %s
            """,
            (
                session["usuario_id"],
            )
        )

        total_receitas = cursor.fetchone()[0]

        # ==========================
        # TOTAL DE DESPESAS
        # ==========================

        cursor.execute(
            """
            SELECT COALESCE(SUM(valor), 0)
            FROM despesas
            WHERE usuario_id = %s
            """
            ,
            (
                session["usuario_id"],
            )
        )

        total_despesas = cursor.fetchone()[0]

        # ==========================
        # TOTAL DE METAS
        # ==========================

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM metas
            WHERE usuario_id = %s
            """
            ,
            (
                session["usuario_id"],
            )
        )

        total_metas = cursor.fetchone()[0]

        # ==========================
        # SALDO
        # ==========================

        saldo = total_receitas - total_despesas

        cursor.close()
        con.close()

        return render_template(
            "dashboard.html",
            total_receitas=total_receitas,
            total_despesas=total_despesas,
            saldo=saldo,
            total_metas=total_metas
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao carregar dashboard.",
            "erro"
        )

        return redirect(
            url_for("home")
        )

# ------------------ Rota para a Página de Receitas ------------------ #
@app.route("/receitas", methods=["GET", "POST"])
def receitas():

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar suas receitas.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    if request.method == "POST":

        descricao = request.form.get("descricao")
        categoria = request.form.get("categoria")
        valor = request.form.get("valor")
        data_recebimento = request.form.get("data_recebimento")
        observacao = request.form.get("observacao")
        recorrente = request.form.get("recorrente") == "on"

        try:

            con = conectar()
            cursor = con.cursor()

            cursor.execute(
                """
                INSERT INTO receitas
                (
                    usuario_id,
                    descricao,
                    categoria,
                    valor,
                    data_recebimento,
                    recorrente,
                    observacao
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    session["usuario_id"],
                    descricao,
                    categoria,
                    valor,
                    data_recebimento,
                    recorrente,
                    observacao
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash(
                "Receita cadastrada com sucesso!",
                "sucesso"
            )

            return redirect(
                url_for("receitas")
            )

        except Exception as erro:

            print("Erro:", erro)

            flash(
                "Erro ao cadastrar receita.",
                "erro"
            )

            return redirect(
                url_for("receitas")
            )

    try:

        con = conectar()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT
                id,
                descricao,
                categoria,
                valor,
                data_recebimento,
                recorrente
            FROM receitas
            WHERE usuario_id = %s
            ORDER BY id DESC
            """,
            (
                session["usuario_id"],
            )
        )

        receitas_usuario = cursor.fetchall()

        cursor.close()
        con.close()

    except Exception as erro:

        print("Erro:", erro)

        receitas_usuario = []

    return render_template(
        "receitas.html",
        receitas=receitas_usuario
    )

# ------------------ Rota para a Página de Editar Receitas ------------------ #  
@app.route("/editar_receita/<int:id>", methods=["GET", "POST"])
def editar_receita(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    try:

        con = conectar()
        cursor = con.cursor()

        if request.method == "POST":

            descricao = request.form.get("descricao")
            categoria = request.form.get("categoria")
            valor = request.form.get("valor")
            data_recebimento = request.form.get("data_recebimento")
            recorrente = request.form.get("recorrente") == "on"
            observacao = request.form.get("observacao")

            cursor.execute(
                """
                UPDATE receitas
                SET
                    descricao = %s,
                    categoria = %s,
                    valor = %s,
                    data_recebimento = %s,
                    recorrente = %s,
                    observacao = %s
                WHERE id = %s
                """,
                (
                    descricao,
                    categoria,
                    valor,
                    data_recebimento,
                    recorrente,
                    observacao,
                    id
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash(
                "Receita atualizada com sucesso!",
                "sucesso"
            )

            return redirect(
                url_for("receitas")
            )

        cursor.execute(
            """
            SELECT
                id,
                descricao,
                categoria,
                valor,
                data_recebimento,
                recorrente,
                observacao
            FROM receitas
            WHERE id = %s
            AND usuario_id = %s
            """,
            (
                id,
                session["usuario_id"]
            )
        )

        receita = cursor.fetchone()

        cursor.close()
        con.close()

        if not receita:

            flash(
                "Receita não encontrada.",
                "erro"
            )

            return redirect(
                url_for("receitas")
            )

        return render_template(
            "editar_receita.html",
            receita=receita
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao editar receita.",
            "erro"
        )

        return redirect(
            url_for("receitas")
        )

# ------------------ Rota para Excluir Receita ------------------ #
@app.route("/excluir_receita/<int:id>")
def excluir_receita(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    try:

        con = conectar()
        cursor = con.cursor()

        # Verifica se a receita pertence ao usuário logado

        cursor.execute(
            """
            SELECT id
            FROM receitas
            WHERE id = %s
            AND usuario_id = %s
            """,
            (
                id,
                session["usuario_id"]
            )
        )

        receita = cursor.fetchone()

        if not receita:

            flash(
                "Receita não encontrada.",
                "erro"
            )

            cursor.close()
            con.close()

            return redirect(
                url_for("receitas")
            )

        # Exclui a receita

        cursor.execute(
            """
            DELETE FROM receitas
            WHERE id = %s
            """,
            (id,)
        )

        con.commit()

        cursor.close()
        con.close()

        flash(
            "Receita excluída com sucesso!",
            "sucesso"
        )

        return redirect(
            url_for("receitas")
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao excluir receita.",
            "erro"
        )

        return redirect(
            url_for("receitas")
        )

# ------------------ Rota para a Página de Despesas ------------------ #
@app.route("/despesas", methods=["GET", "POST"])
def despesas():

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar suas despesas.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    # =====================================
    # CADASTRAR DESPESA
    # =====================================

    if request.method == "POST":

        descricao = request.form.get("descricao")
        categoria = request.form.get("categoria")
        valor = request.form.get("valor")
        data_lancamento = request.form.get("data_lancamento")
        data_vencimento = request.form.get("data_vencimento")
        data_pagamento = request.form.get("data_pagamento")
        status = request.form.get("status")
        observacao = request.form.get("observacao")

        try:

            con = conectar()
            cursor = con.cursor()

            cursor.execute(
                """
                INSERT INTO despesas
                (
                    usuario_id,
                    descricao,
                    categoria,
                    valor,
                    data_lancamento,
                    data_vencimento,
                    data_pagamento,
                    status,
                    observacao
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    session["usuario_id"],
                    descricao,
                    categoria,
                    valor,
                    data_lancamento,
                    data_vencimento if data_vencimento else None,
                    data_pagamento if data_pagamento else None,
                    status,
                    observacao
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash(
                "Despesa cadastrada com sucesso!",
                "sucesso"
            )

            return redirect(
                url_for("despesas")
            )

        except Exception as erro:

            print("Erro:", erro)

            flash(
                "Erro ao cadastrar despesa.",
                "erro"
            )

            return redirect(
                url_for("despesas")
            )

    # =====================================
    # LISTAR DESPESAS
    # =====================================

    try:

        con = conectar()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT
                id,
                descricao,
                categoria,
                valor,
                data_vencimento,
                status
            FROM despesas
            WHERE usuario_id = %s
            ORDER BY id DESC
            """,
            (
                session["usuario_id"],
            )
        )

        despesas_usuario = cursor.fetchall()

        cursor.close()
        con.close()

    except Exception as erro:

        print("Erro:", erro)

        despesas_usuario = []

    return render_template(
        "despesas.html",
        despesas=despesas_usuario
    )

# ------------------ Rota para editar Despesas ------------------ #

@app.route("/editar_despesa/<int:id>", methods=["GET", "POST"])
def editar_despesa(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    try:

        con = conectar()
        cursor = con.cursor()

        if request.method == "POST":

            descricao = request.form.get("descricao")
            categoria = request.form.get("categoria")
            valor = request.form.get("valor")
            data_lancamento = request.form.get("data_lancamento")
            data_vencimento = request.form.get("data_vencimento")
            data_pagamento = request.form.get("data_pagamento")
            status = request.form.get("status")
            observacao = request.form.get("observacao")

            cursor.execute(
                """
                UPDATE despesas
                SET
                    descricao = %s,
                    categoria = %s,
                    valor = %s,
                    data_lancamento = %s,
                    data_vencimento = %s,
                    data_pagamento = %s,
                    status = %s,
                    observacao = %s
                WHERE id = %s
                """
                ,
                (
                    descricao,
                    categoria,
                    valor,
                    data_lancamento,
                    data_vencimento if data_vencimento else None,
                    data_pagamento if data_pagamento else None,
                    status,
                    observacao,
                    id
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash(
                "Despesa atualizada com sucesso!",
                "sucesso"
            )

            return redirect(
                url_for("despesas")
            )

        cursor.execute(
            """
            SELECT
                id,
                descricao,
                categoria,
                valor,
                data_lancamento,
                data_vencimento,
                data_pagamento,
                status,
                observacao
            FROM despesas
            WHERE id = %s
            AND usuario_id = %s
            """,
            (
                id,
                session["usuario_id"]
            )
        )

        despesa = cursor.fetchone()

        cursor.close()
        con.close()

        if not despesa:

            flash(
                "Despesa não encontrada.",
                "erro"
            )

            return redirect(
                url_for("despesas")
            )

        return render_template(
            "editar_despesa.html",
            despesa=despesa
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao editar despesa.",
            "erro"
        )

        return redirect(
            url_for("despesas")
        )

# ------------------ Rota para excluir despesas ------------------ #

@app.route("/excluir_despesa/<int:id>")
def excluir_despesa(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    try:

        con = conectar()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT id
            FROM despesas
            WHERE id = %s
            AND usuario_id = %s
            """,
            (
                id,
                session["usuario_id"]
            )
        )

        despesa = cursor.fetchone()

        if not despesa:

            flash(
                "Despesa não encontrada.",
                "erro"
            )

            cursor.close()
            con.close()

            return redirect(
                url_for("despesas")
            )

        cursor.execute(
            """
            DELETE FROM despesas
            WHERE id = %s
            """,
            (id,)
        )

        con.commit()

        cursor.close()
        con.close()

        flash(
            "Despesa excluída com sucesso!",
            "sucesso"
        )

        return redirect(
            url_for("despesas")
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao excluir despesa.",
            "erro"
        )

        return redirect(
            url_for("despesas")
        )    
# ------------------ Rota para a Página de Metas ------------------ #
@app.route("/metas", methods=["GET", "POST"])
def metas():

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar suas metas.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    # =====================================
    # CADASTRAR META
    # =====================================

    if request.method == "POST":

        titulo = request.form.get("titulo")
        descricao = request.form.get("descricao")
        valor_meta = request.form.get("valor_meta")
        valor_atual = request.form.get("valor_atual")
        data_inicio = request.form.get("data_inicio")
        data_limite = request.form.get("data_limite")
        status = request.form.get("status")

        try:

            con = conectar()
            cursor = con.cursor()

            cursor.execute(
                """
                INSERT INTO metas
                (
                    usuario_id,
                    titulo,
                    descricao,
                    valor_meta,
                    valor_atual,
                    data_inicio,
                    data_limite,
                    status
                )
                VALUES
                (
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s,
                    %s
                )
                """,
                (
                    session["usuario_id"],
                    titulo,
                    descricao,
                    valor_meta,
                    valor_atual,
                    data_inicio if data_inicio else None,
                    data_limite if data_limite else None,
                    status
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash(
                "Meta cadastrada com sucesso!",
                "sucesso"
            )

            return redirect(
                url_for("metas")
            )

        except Exception as erro:

            print("Erro:", erro)

            flash(
                "Erro ao cadastrar meta.",
                "erro"
            )

            return redirect(
                url_for("metas")
            )

    # =====================================
    # LISTAR METAS
    # =====================================

    try:

        con = conectar()
        cursor = con.cursor()

        cursor.execute(
            """
            SELECT
                id,
                titulo,
                valor_meta,
                valor_atual,
                data_limite,
                status
            FROM metas
            WHERE usuario_id = %s
            ORDER BY id DESC
            """,
            (
                session["usuario_id"],
            )
        )

        metas_usuario = cursor.fetchall()

        cursor.close()
        con.close()

    except Exception as erro:

        print("Erro:", erro)

        metas_usuario = []

    return render_template(
        "metas.html",
        metas=metas_usuario
    )


# ------------------ Rota para Editar Metas ------------------ #
@app.route("/editar_meta/<int:id>", methods=["GET", "POST"])
def editar_meta(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    try:

        con = conectar()
        cursor = con.cursor()

        # ==========================
        # SALVAR ALTERAÇÕES
        # ==========================

        if request.method == "POST":

            titulo = request.form.get("titulo")
            descricao = request.form.get("descricao")
            valor_meta = request.form.get("valor_meta")
            valor_atual = request.form.get("valor_atual")
            data_inicio = request.form.get("data_inicio")
            data_limite = request.form.get("data_limite")
            status = request.form.get("status")

            cursor.execute(
                """
                UPDATE metas
                SET
                    titulo = %s,
                    descricao = %s,
                    valor_meta = %s,
                    valor_atual = %s,
                    data_inicio = %s,
                    data_limite = %s,
                    status = %s
                WHERE id = %s
                """,
                (
                    titulo,
                    descricao,
                    valor_meta,
                    valor_atual,
                    data_inicio if data_inicio else None,
                    data_limite if data_limite else None,
                    status,
                    id
                )
            )

            con.commit()

            cursor.close()
            con.close()

            flash(
                "Meta atualizada com sucesso!",
                "sucesso"
            )

            return redirect(
                url_for("metas")
            )

        # ==========================
        # CARREGAR META
        # ==========================

        cursor.execute(
            """
            SELECT
                id,
                titulo,
                descricao,
                valor_meta,
                valor_atual,
                data_inicio,
                data_limite,
                status
            FROM metas
            WHERE id = %s
            AND usuario_id = %s
            """,
            (
                id,
                session["usuario_id"]
            )
        )

        meta = cursor.fetchone()

        cursor.close()
        con.close()

        if not meta:

            flash(
                "Meta não encontrada.",
                "erro"
            )

            return redirect(
                url_for("metas")
            )

        return render_template(
            "editar_meta.html",
            meta=meta
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao editar meta.",
            "erro"
        )

        return redirect(
            url_for("metas")
        )
# ------------------ Rota para Excluir Meta ------------------ #
@app.route("/excluir_meta/<int:id>")
def excluir_meta(id):

    if "usuario_id" not in session:

        flash(
            "Faça login para acessar esta área.",
            "erro"
        )

        return redirect(
            url_for("login")
        )

    try:

        con = conectar()
        cursor = con.cursor()

        # Verifica se a meta pertence ao usuário logado

        cursor.execute(
            """
            SELECT id
            FROM metas
            WHERE id = %s
            AND usuario_id = %s
            """,
            (
                id,
                session["usuario_id"]
            )
        )

        meta = cursor.fetchone()

        if not meta:

            flash(
                "Meta não encontrada.",
                "erro"
            )

            cursor.close()
            con.close()

            return redirect(
                url_for("metas")
            )

        # Exclusão

        cursor.execute(
            """
            DELETE FROM metas
            WHERE id = %s
            """,
            (id,)
        )

        con.commit()

        cursor.close()
        con.close()

        flash(
            "Meta excluída com sucesso!",
            "sucesso"
        )

        return redirect(
            url_for("metas")
        )

    except Exception as erro:

        print("Erro:", erro)

        flash(
            "Erro ao excluir meta.",
            "erro"
        )

        return redirect(
            url_for("metas")
        )

# ------------------ Conexão com o Banco de Dados ------------------ #
try:

    con = conectar()

    print("✅ Conectado ao PostgreSQL com sucesso!")

    con.close()

except Exception as erro:

    print("❌ Erro ao conectar:", erro)

# ------------------ Execução da Aplicação Local ------------------ #
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

import psycopg2


def conectar():

    conexao = psycopg2.connect(
        host="localhost",
        database="financeweb",
        user="postgres",
        password="FinanceWeb2026",
        port="5432"
    )

    return conexao
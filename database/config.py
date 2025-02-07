import sqlite3

DB_PATH = 'dados.db'

def criar_tabela():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
    id INTEGET PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    email TEXT NOT NULL
    interesse TEXT NOT NULL
    numero TEXT NOT NULL
    cidade TEXT NOT NULL
    estado TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


def salvar_contato(nome, email, interesse, numero, cidade, estado):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO contatos (nome, email, interesse, numero, cidade, estado)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, email, interesse, numero, cidade, estado))
    conn.commit()
    conn.close()
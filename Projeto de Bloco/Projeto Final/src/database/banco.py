import sqlite3

DB_PATH = 'biblioteca.db'

def conectar():

    """
    Centralizar a conexão do banco em uma única função
    """

    return sqlite3.connect(DB_PATH)

def criar_banco():

    """

    Criar e definir tabelas do banco de dados sqlite
    
    """

    conn = conectar()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS autores (
                    id_autor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    pais_origem TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS livros (
                    id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    ISBN TEXT NOT NULL UNIQUE,
                    genero TEXT NOT NULL,
                    data_publicacao DATE NOT NULL,
                    qtd_paginas INTEGER NOT NULL,
                    disponibilidade INTEGER NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    sobrenome TEXT NOT NULL,
                    data_nascimento DATE NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS emprestimos (
                    id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_livro INTEGER NOT NULL,
                    id_usuario INTEGER NOT NULL,
                    data_emprestimo DATE NOT NULL,
                    data_devolucao DATE,
                    FOREIGN KEY (id_livro) REFERENCES livros(id_livro) ON DELETE CASCADE,
                    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario) ON DELETE CASCADE)''')

    c.execute('''CREATE TABLE IF NOT EXISTS livrosautores (
                    id_livro INTEGER NOT NULL,
                    id_autor INTEGER NOT NULL,
                    PRIMARY KEY (id_livro, id_autor),
                    FOREIGN KEY (id_livro) REFERENCES livros(id_livro) ON DELETE CASCADE,
                    FOREIGN KEY (id_autor) REFERENCES autores(id_autor) ON DELETE CASCADE)''')

    conn.commit()
    conn.close()

    
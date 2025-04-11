from src.database.banco import conectar

def consultar_livros_db():
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute("SELECT * FROM livros")
        livros = c.fetchall()
        return livros
    
    finally:
        conn.close()

def buscar_livro(id_livro):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute("SELECT * FROM livros WHERE id_livro = ?", (id_livro,))
        livro = c.fetchone()
        return livro
    
    finally:
        conn.close()

def verificar_livro_existente(isbn= None, id_livro= None ):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        if not isbn == None:
            c.execute("SELECT id_livro FROM livros WHERE isbn = ?", (isbn,))
            livro = c.fetchone()
            return livro
        
        if not id_livro == None:
            c.execute("SELECT disponibilidade FROM livros WHERE id_livro = ?", (id_livro,))
            livro = c.fetchone()
            return livro
    
    finally:
        conn.close()

def inserir_livro(titulo, isbn, genero, data_publicacao, qtd_paginas, disponibilidade):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute("""
        INSERT INTO livros (titulo, isbn, genero, data_publicacao, qtd_paginas, disponibilidade)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (titulo, isbn, genero, data_publicacao, qtd_paginas, disponibilidade))
        
        id_livro = c.lastrowid

        conn.commit()
        return id_livro
    finally:
        conn.close()

def inserir_livros_autores(id_livro, id_autor):
    try:        
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute("SELECT 1 FROM livrosautores WHERE id_livro = ? AND id_autor = ?", (id_livro, id_autor))
        relacao = c.fetchone()

        if not relacao:
            c.execute("INSERT INTO livrosautores (id_livro, id_autor) VALUES (?, ?)", (id_livro, id_autor))

        conn.commit()
    finally:
        conn.close()
    
def atualizar_livro_db(id_livro, campo, valor):
    try:
        conn = conectar()
        c = conn.cursor()
        query = f"UPDATE livros SET {campo} = ? WHERE id_livro = ?"
        c.execute(query, (valor, id_livro))
        conn.commit()
        linhas = c.rowcount
        return linhas
    
    finally:
        conn.close()

def excluir_livro_db(id_livro):
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute("DELETE FROM livros WHERE id_livro = ?", (id_livro,))
        conn.commit()
    finally:
        conn.close()

def diminuir_disponibilidade(id_livro):
    try:       
        conn = conectar()
        c = conn.cursor()     
                
        c.execute(
        "UPDATE livros SET disponibilidade = disponibilidade - 1 WHERE id_livro = ?",
        (id_livro,)
        )
        conn.commit()
    finally:
        conn.close()

def aumentar_disponibilidade(id_livro):
    try:       
        conn = conectar()
        c = conn.cursor()     
                
        c.execute(
        "UPDATE livros SET disponibilidade = disponibilidade + 1 WHERE id_livro = ?",
        (id_livro,)
        )
        conn.commit()
    finally:
        conn.close()



    
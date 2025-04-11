from src.database.banco import conectar

def consultar_autores_db():
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute("SELECT * FROM autores")
        autores = c.fetchall()
        return autores
    
    finally:
        conn.close()

def buscar_autor(id_autor):

    conn = conectar()
    c = conn.cursor()

    c.execute("SELECT * FROM autores WHERE id_autor = ?", (id_autor,))
    autor = c.fetchone()   
    return autor

def buscar_autor_por_nome(nome, pais_origem):
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute("SELECT id_autor FROM autores WHERE nome = ? AND pais_origem = ?", (nome, pais_origem))
        autor = c.fetchone()

        return autor
    finally:
        conn.close()

def inserir_autor(nome, pais_origem):
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute("INSERT INTO autores (nome, pais_origem) VALUES (?, ?)", (nome, pais_origem))
        conn.commit()
        id_autor = c.lastrowid

        return id_autor
    finally:
        conn.close()

def atualizar_autor_db(id_autor, campo, valor):
    try:
        conn = conectar()
        c = conn.cursor()
        query = f"UPDATE autores SET {campo} = ? WHERE id_autor = ?"
        c.execute(query, (valor, id_autor))
        conn.commit()
        linhas = c.rowcount
        return linhas
    
    finally:
        conn.close()

def verificar_relacao_livro_autor(id_autor):    
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute("SELECT 1 FROM livrosautores WHERE id_autor = ?", (id_autor,))
        relacao = c.fetchone()

        return relacao
    finally:
        conn.close()

def excluir_autor_db(id_autor):
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute("DELETE FROM autores WHERE id_autor = ?", (id_autor,))
        conn.commit()     

    finally:
        conn.close() 




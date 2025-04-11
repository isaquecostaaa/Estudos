from src.database.banco import conectar
from datetime import datetime

def buscar_emprestimos():
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute("SELECT * FROM emprestimos")
        emprestimos = c.fetchall()
        return emprestimos
    
    finally:
        conn.close()

def buscar_emprestimo(id_emprestimo):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute('''
        SELECT id_emprestimo, data_devolucao 
        FROM emprestimos 
        WHERE id_emprestimo = ?
        ''', (id_emprestimo,))

        emprestimo = c.fetchone()
        return emprestimo
    finally:
        conn.close()

def buscar_usuarios_emprestimos(id_livro, id_usuario):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute('''
        SELECT 
            l.titulo, 
            u.nome, 
            u.sobrenome
        FROM 
            livros l,
            usuarios u
        WHERE 
            l.id_livro = ? AND 
            u.id_usuario = ?
        ''', (id_livro, id_usuario))
        resultado = c.fetchone()
        return resultado
    finally:
        conn.close()

def verificar_emprestimos_ativos(id_usuario= None, id_livro= None, id_emprestimo= None):
    try:    
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()


        if not id_usuario == None:
            c.execute('''
                SELECT COUNT(*) FROM emprestimos 
                WHERE id_usuario = ? AND data_devolucao IS NULL
            ''', (id_usuario,))
            emprestimos_ativos = c.fetchone()[0]
        
        if not id_livro == None:
            c.execute("""SELECT COUNT(*) FROM emprestimos 
            WHERE id_livro = ? AND data_devolucao IS NULL""", (id_livro,))
            emprestimos_ativos = c.fetchone()[0]
        
        if not id_emprestimo == None:
            c.execute("""SELECT COUNT(*) FROM emprestimos 
            WHERE id_livro = ? AND data_devolucao IS NULL""", (id_livro,))
            emprestimos_ativos = c.fetchone()[0]

        return emprestimos_ativos

    finally:
        conn.close()

def inserir_emprestimo(id_livro, id_usuario):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute(
        "INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo) VALUES (?, ?, ?)",
        (id_livro, id_usuario, datetime.now().date())
        )
    finally:
        conn.close()

def atualizar_emprestimo_db(id_emprestimo, campo, valor):
    try:
        conn = conectar()
        c = conn.cursor()
        query = f"UPDATE emprestimos SET {campo} = ? WHERE id_emprestimo = ?"
        c.execute(query, (valor, id_emprestimo))
        conn.commit()
        linhas = c.rowcount
        return linhas
    
    finally:
        conn.close()

def excluir_emprestimo_db(id_emprestimo):
    try:
        conn = conectar()
        c = conn.cursor()

        c.execute('''
        DELETE FROM emprestimos
        WHERE id_emprestimo = ?
        ''', (id_emprestimo,))
                
        conn.commit()
    finally:
        conn.close()

        









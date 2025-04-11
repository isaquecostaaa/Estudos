from src.database.banco import conectar

def consultar_usuarios_db():
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute("SELECT * FROM usuarios")
        usuarios = c.fetchall()
        return usuarios
    finally:
        conn.close()

def deletar_usuario(id_usuario):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute('''
            DELETE FROM usuarios
            WHERE id_usuario = ?
        ''', (id_usuario,))
        conn.commit()
        deletados = c.rowcount
        return deletados
    
    finally:
        conn.close()

def buscar_usuario(id_usuario):
    try:
        conn = conectar()
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        resultado = c.fetchone()
        return resultado
    
    finally:
        conn.close()

def atualizar_usuario_db(id_usuario, campo, valor):
    try:
        conn = conectar()
        c = conn.cursor()
        query = f"UPDATE usuarios SET {campo} = ? WHERE id_usuario = ?"
        c.execute(query, (valor, id_usuario))
        conn.commit()
        linhas = c.rowcount
        return linhas
    
    finally:
        conn.close()

def cadastrar_usuario_db(nome, sobrenome, data_nascimento):
    try:    
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute(
            "INSERT INTO usuarios (nome, sobrenome, data_nascimento) VALUES (?, ?, ?)",
            (nome, sobrenome, data_nascimento)
        )
        conn.commit()

    finally:
        conn.close()

def verificar_usuarios_existente(id_usuario):
    try:
        conn = conectar()
        conn.execute("PRAGMA foreign_keys = ON")
        c = conn.cursor()

        c.execute("SELECT id_usuario FROM usuarios WHERE id_usuario = ?", (id_usuario,))
        resultado = c.fetchone()
        return resultado
    finally:
        conn.close()
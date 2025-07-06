# Importacion de Libreria
import sqlite3 as sql
import streamlit as st

# Funciones de Creacion de Tablas

def SQL_usuarios_tabla(directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Crear la tabla 'server' si no existe
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            pw TEXT NOT NULL,
            UNIQUE(username))
    """)
    conexion.commit() # Guardar los cambios
    cursor.close() # Cerrar el cursor
    conexion.close() # Cerrar la conexion

def SQL_server_tabla(directorio: str ="src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Crear la tabla 'server' si no existe
    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS server (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            variable TEXT NOT NULL,
            valor TEXT NOT NULL,
            UNIQUE(variable))
    """)
    # Insertar contador de usos si no existe con valor 0
    cursor.execute("""INSERT OR IGNORE INTO server (variable, valor) VALUES ('despliegues', '0')""")
    # Actualizar valor del contador de usos a contador + 1
    if 'despliegue' not in st.session_state:
        if cursor.execute("SELECT * FROM usuarios WHERE username = 'ADMIN'").fetchall(): 
            cursor.execute("""UPDATE server SET valor = CAST(valor AS INTEGER) + 1 WHERE variable = 'despliegues'""")
    conexion.commit() # Guardar los cambios
    cursor.close() # Cerrar el cursor
    conexion.close() # Cerrar la conexion

def SQL_consultaEspecifica(parametro: str, condicion: str, tabla: str, columna: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Consultar el valor de la variable en la tabla
    cursor.execute(f"SELECT {columna} FROM {tabla} WHERE {condicion} = ?", (parametro,))
    resultado = cursor.fetchone()
    cursor.close() # Cerrar el cursor
    conexion.close() # Cerrar la conexion
    return resultado[0] if resultado else None  # Retornar el valor encontrado o None si no existe

def SQL_consultaGeneral(tabla: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Consultar todos los registros de la tabla
    cursor.execute(f"SELECT * FROM {tabla}")
    resultados = cursor.fetchall()
    cursor.close() # Cerrar el cursor
    conexion.close() # Cerrar la conexion
    return resultados  # Retornar todos los registros encontrados

def SQL_crearUsuario(nombre: str, pw: str, token: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    if cursor.execute("SELECT username FROM usuarios WHERE username = 'ADMIN'").fetchall():
        if token == cursor.execute("SELECT pw FROM usuarios WHERE username = 'ADMIN'").fetchall()[0]:
            cursor.execute("INSERT OR IGNORE INTO usuarios (username, pw) VALUES (?, ?)", (nombre, pw,))
            print("Usuario creado con token")
    else:
        cursor.execute("INSERT OR IGNORE INTO usuarios (username, pw) VALUES (?, ?)", (nombre, pw,))
        cursor.execute("""UPDATE server SET valor = CAST(valor AS INTEGER) + 1 WHERE variable = 'despliegues'""")
        print("Usuario creado sin tokens")
    conexion.commit()
    return None
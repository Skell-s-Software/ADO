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
            cargo TEXT NOT NULL,
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

def SQL_chat_tabla(directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Crear la tabla para almacenar mensajes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT NOT NULL,
            mensaje TEXT NOT NULL)            
    """)
    cursor.close()
    conexion.close()

def SQL_clientes_tabla(directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Crear tabla para guardar los clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cedula INTEGER NOT NULL,
            codigoSocio INTEGER,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            correo TEXT,
            direccion TEXT,
            descripcion TEXT)
    """)
    cursor.close()
    conexion.close()

def SQL_productos_tabla(directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Creacion de la tabla
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo INTEGER NOT NULL,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL)
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stack(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo INTEGER NOT NULL,
            inventario TEXT NOT NULL,
            FOREIGN KEY (codigo) REFERENCES productos(codigo))
    """)
    conexion.commit()
    cursor.close()
    conexion.close()

def SQL_consultaEspecifica(parametro: str, condicion: str, tabla: str, columna: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Consultar el valor de la variable en la tabla
    cursor.execute(f"SELECT {columna} FROM {tabla} WHERE {condicion} = ?", (parametro,))
    resultado = cursor.fetchone()
    cursor.close() # Cerrar el cursor
    conexion.close() # Cerrar la conexion
    return resultado[0] if resultado else None  # Retornar el valor encontrado o None si no existe

def SQL_consultaFila(parametro: str, condicion: str, tabla: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Consultar el valor de la variable en la tabla
    cursor.execute(f"SELECT * FROM {tabla} WHERE {condicion} = ?", (parametro,))
    resultado = cursor.fetchone()
    cursor.close() # Cerrar el cursor
    conexion.close() # Cerrar la conexion
    return resultado if resultado else None  # Retornar el valor encontrado o None si no existe

def SQL_consultaGeneral(tabla: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Consultar todos los registros de la tabla
    cursor.execute(f"SELECT * FROM {tabla}")
    resultados = cursor.fetchall()
    cursor.close() # Cerrar el cursor
    conexion.close() # Cerrar la conexion
    return resultados  # Retornar todos los registros encontrados

def SQL_crearUsuario(nombre: str, pw: str, token: str="token", cargo: str="Expulsar", directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    # Verifica si existe el usuario ADMIN
    admin_pw_row = cursor.execute("SELECT pw FROM usuarios WHERE username = 'ADMIN'").fetchone()
    admin_exists = admin_pw_row is not None
    if not admin_exists and nombre == 'ADMIN':
        # Si no existe ADMIN y se está creando ADMIN, lo crea
        cursor.execute("INSERT INTO usuarios (username, pw, cargo) VALUES (?, ?, ?)", (nombre, pw, cargo))
        cursor.execute("""UPDATE server SET valor = CAST(valor AS INTEGER) + 1 WHERE variable = 'despliegues'""")
        print("Usuario ADMIN creado")
    elif admin_exists:
        # Si ADMIN existe, verifica el token para crear cualquier usuario
        admin_pw = admin_pw_row[0]
        if token == admin_pw:
            cursor.execute("INSERT INTO usuarios (username, pw, cargo) VALUES (?, ?, ?)", (nombre, pw, cargo))
            print("Usuario creado con token")
        else:
            print("Token incorrecto, usuario no creado")
    else:
        print("Primero debe crearse el usuario ADMIN")
    conexion.commit()
    cursor.close()
    conexion.close()
    return None

def SQL_guardarMensaje(user: str, mensaje: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO chat (usuario, mensaje) VALUES (?, ?)", (user, mensaje))
    conexion.commit()
    cursor.close()
    conexion.close()

def SQL_crearCliente(cedula: int, nombre: str, telefono: str, correo: str = None, direccion: str = None, descripcion: str = None, codigo: str = None, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO clientes (cedula, codigoSocio, nombre, telefono, correo, direccion, descripcion) VALUES (?, ?, ?, ?, ?, ?, ?)", (cedula, codigo, nombre, telefono, correo, direccion, descripcion))
    conexion.commit()
    cursor.close()
    conexion.close()

def SQL_edicionEspecifica(seleccion: str, dato: str, cedula: str, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    cursor.execute(f"UPDATE clientes SET {seleccion.lower().replace(" ", "")} = ? WHERE cedula = ?", (dato, cedula))
    conexion.commit()
    cursor.close()
    conexion.close()

def SQL_crearProducto(codigo: str, nombre: str, precio: str, descripcion: str = None, directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO productos (codigo, nombre, descripcion, precio) VALUES (?, ?, ?, ?)", (codigo, nombre, descripcion, precio))
    conexion.commit()
    cursor.execute("INSERT INTO stack (codigo, inventario) VALUES (?, ?)", (codigo, "0"))
    conexion.commit()
    cursor.close()
    conexion.close()

def SQL_listadoProductos(directorio: str = "src/database/ado.db"):
    conexion = sql.connect(directorio)
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT productos.*, stack.inventario
        FROM productos
        LEFT JOIN stack ON productos.codigo = stack.codigo
    """)
    resultados = cursor.fetchall()
    cursor.close()
    conexion.close()
    return resultados
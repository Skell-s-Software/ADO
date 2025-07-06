# Modulo de Registro de Usuario

# Importacion de Librerias
import streamlit as st
from streamlit_option_menu import option_menu as stmenu

# Importacion de Constantes
from constantes import TITULO_LOGIN

# Importacion de Modulos
from modules.database import SQL_consultaEspecifica, SQL_crearUsuario
from time import sleep

# Funciones Internas
def pagina_login():
    st.title(TITULO_LOGIN)
    pestana = stmenu(
        None,
        ["Iniciar Sesion", "Registrarse"],
        icons = ['person-fill', 'person-fill-add'],
        default_index=0,
        orientation="horizontal"
    )
    if pestana == "Iniciar Sesion":
        with st.form( # Formulario de Inicio de Sesion
            key='login',
            clear_on_submit=True,
            enter_to_submit=False,
            border=True
            ):
            username = st.text_input(
                "Nombre de Usuario",
                help="Escriba su nombre de usuario aqui",
                placeholder="Escriba su nombre de usuario.",
                icon=":material/person:"
            )
            pw = st.text_input(
                "Contrasena de Usuario",
                type='password',
                help="Escriba su contrasena de usuario aqui",
                placeholder="Escriba su contrasena de usuario.",
                icon=":material/password:"
            )
            if st.form_submit_button(
                "Iniciar Sesion",
                help="Al presionar este boton, si los datos son correctos, iniciara sesion exitosamente.",
                type="primary",
                icon=":material/login:",
                use_container_width=True
                ):
                if SQL_consultaEspecifica(username, "username", "usuarios", "username"):
                    st.session_state.usuario = username
                    st.session_state.cargo = SQL_consultaEspecifica(username, "username", "usuarios", "cargo")
                    st.success("Inicio Exitoso")
                    sleep(1)
                    st.rerun()
                else:
                    st.error("Ha ocurrido un error")
    else:
        with st.form( # Formulario de Creacion de Usuario
            key='registro',
            clear_on_submit=True,
            enter_to_submit=False,
            border=True
            ):
            username = st.text_input(
                "Nombre de Usuario",
                help="Escriba su nombre de usuario aqui",
                placeholder="Escriba su nombre de usuario.",
                icon=":material/person:"
            )
            pw = st.text_input(
                "Contrasena de Usuario",
                type='password',
                help="Escriba su contrasena de usuario aqui",
                placeholder="Escriba su contrasena de usuario.",
                icon=":material/password:"
            )
            pw2 = st.text_input(
                "Confirmar Contrasena de Usuario",
                type='password',
                help="Escriba su contrasena de usuario aqui",
                placeholder="Escriba su contrasena de usuario.",
                icon=":material/password:"
            )
            token = st.text_input(
                "Contrasena del Usuario Administrador",
                type='password',
                help="Escriba la contrasena del usuario administrador aqui",
                placeholder="Contrasena del Usuario Administrador.",
                icon=":material/lock_person:"
            )
            cargo = st.selectbox(
                "Cargo del Usuario a Registrar",
                options=["Gestor Principal", "Gestor de Inventario", "Punto de Venta", "Gestor de Clientes"],
                index=0,
                help="Seleccione el cargo que desea asignar al usuario.",
                placeholder="Cargo a Asignar al usuario"
            )
            if st.form_submit_button(
                "Registrar Usuario",
                help="Al presionar este boton, si los datos son correctos, su usuario sera registrado.",
                type="primary",
                icon=":material/person_add:",
                use_container_width=True
                ):
                if len(pw) > 8 and pw == pw2 and username and token:
                    SQL_crearUsuario(username, pw, token, cargo)
                    st.success("Registro de Usuario exitoso, ahora dirigase a iniciar sesion")
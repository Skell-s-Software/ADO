# Modulo de Registro de Usuario

# Importacion de Librerias
import streamlit as st
from streamlit_option_menu import option_menu as stmenu

# Importacion de Constantes
from constantes import TITULO_LOGIN

# Importacion de Modulos
from modules.database import SQL_server_tabla, SQL_consultaEspecifica

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
        with st.form(
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
                icon=":material/person:"
            )
            if st.form_submit_button("Iniciar Sesion"):
                st.success("Inicio Exitoso")
    else:
        with st.form(
            key='registro',
            clear_on_submit=True,
            enter_to_submit=True,
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
                icon=":material/person:"
            )
            pw2 = st.text_input(
                "Confirmar Contrasena de Usuario",
                type='password',
                help="Escriba su contrasena de usuario aqui",
                placeholder="Escriba su contrasena de usuario.",
                icon=":material/person:"
            )
            if st.form_submit_button("Registrar Usuario"):
                st.success("Inicio Exitoso")
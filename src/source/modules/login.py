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
@st.dialog("¿Estás seguro de que deseas cerrar la sesión?")
def dialog_logout():
    CERRAR = st.button("Cerrar Sesion",
                type = 'primary',
                use_container_width = True,
                key = 'Cerrar'
            )
    CANCELAR = st.button("Cancelar",
                    type = 'secondary',
                    use_container_width = True,
                    key = 'Cancelar'
                )
    if CERRAR or CANCELAR:
        if CERRAR:
            del st.session_state.usuario
            del st.session_state.cargo
        st.rerun()

def pagina_login():
    st.title(TITULO_LOGIN)
    pestana = stmenu(
        None,
        ["Iniciar Sesión", "Registrarse"],
        icons = ['person-fill', 'person-fill-add'],
        default_index=0,
        orientation="horizontal"
    )
    if pestana == "Iniciar Sesión":
        with st.form( # Formulario de Inicio de Sesion
            key='login',
            clear_on_submit=True,
            enter_to_submit=False,
            border=True
            ):
            username = st.text_input(
                "Nombre de Usuario",
                help="Escriba aquí su nombre de usuario, puede contener cualquier carácter.",
                placeholder="Escriba su nombre de usuario aquí.",
                icon=":material/person:"
            )
            pw = st.text_input(
                "Contraseña de Usuario",
                type='password',
                help="Escriba aquí su contraseña de usuario.",
                placeholder="Escriba su contraseña de usuario aquí.",
                icon=":material/password:"
            )
            if st.form_submit_button(
                "Iniciar Sesión",
                help="Al presionar este boton y los datos son correctos, iniciará sesión exitosamente.",
                type="primary",
                icon=":material/login:",
                use_container_width=True
                ):
                if SQL_consultaEspecifica(username, "username", "usuarios", "username"):
                    st.session_state.usuario = username
                    st.session_state.cargo = SQL_consultaEspecifica(username, "username", "usuarios", "cargo")
                    st.success("¡Inicio Exitoso! Redirigiendo...")
                    sleep(1)
                    st.rerun()
                else:
                    st.error("Ha ocurrido un error, asegurese de escribir correctamente sus datos.")
    else:
        with st.form( # Formulario de Creacion de Usuario
            key='registro',
            clear_on_submit=True,
            enter_to_submit=False,
            border=True
            ):
            username = st.text_input(
                "Nombre de Usuario",
                help="Escriba aquí el nombre de usuario a registrar.",
                placeholder="Escriba el nombre de usuario a registrar.",
                icon=":material/person:"
            )
            pw = st.text_input(
                "Contraseña de Usuario",
                type='password',
                help="Escriba aquí la contraseña del usuario a registrar.",
                placeholder="Escriba la contraseña del usuario a registrar.",
                icon=":material/password:"
            )
            pw2 = st.text_input(
                "Confirmar Contraseña",
                type='password',
                help="Escriba aquí nuevamente la contraseña del usuario a registrar, para confirmar que la recuerda correctamente.",
                placeholder="Escriba nuevamente la contraseña.",
                icon=":material/password:"
            )
            token = st.text_input(
                "Contraseña del Administrador",
                type='password',
                help="Escriba aquí la contraseña del Administrador para confirmar su registro.",
                placeholder="Escriba la contraseña del Administrador.",
                icon=":material/lock_person:"
            )
            cargo = st.selectbox(
                "Cargo del Usuario a Registrar",
                options=["Gestor Principal", "Gestor de Inventario", "Punto de Venta", "Gestor de Clientes"],
                index=0,
                help="Seleccione el cargo que desea asignar al usuario que va a registrar.",
                placeholder="Cargo a Asignar al usuario"
            )
            if st.form_submit_button(
                "Registrar Usuario",
                help="Al presionar este botón y los datos son correctos, su usuario sera registrado.",
                type="primary",
                icon=":material/person_add:",
                use_container_width=True
                ):
                if len(pw) > 8:
                    if pw == pw2:
                        if username and token:
                            try:
                                SQL_crearUsuario(username, pw, token, cargo)
                                st.success("Registro de Usuario exitoso, ahora dirigase a iniciar sesion")
                            except:
                                st.error("Contraseña del Administrador incorrecta o error interno del servidor, intentelo nuevamente.")
                        else:
                            st.error("¡Olvidó escribir algo! Intentelo nuevamente y asegurese de escribir todos los campos solicitados.")
                    else:
                        st.error("Las contraseñas proporcionadas no coinciden, intentelo nuevamente.")
                else:
                    st.error("La contraseña debe contener minimo 8 carácteres, intentelo nuevamente.")
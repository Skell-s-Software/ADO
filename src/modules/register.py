# Modulo de Registro
# Este modulo se encarga de realizar la instalacion de la aplicacion dentro del sistema.
# Este modulo no es necesario para el funcionamiento de la aplicacion, pero si para su instalacion.
# Cuando no hay despliegues mayores a 1, se considera que la aplicacion no esta instalada.
# En caso positivo se procede a realizar la instalacion de la aplicacion.
# Se crea un token para el usuario principal que es el que controla los permisos de registro entre otros.

# Importacion de Librerias
import streamlit as st

# Importacion de Constantes
from constantes import TITULO_REGISTRO, TEXTO_REGISTRO

# Importacion de Modulos
from modules.database import SQL_crearUsuario
from time import sleep

# Funciones Internas
def pagina_instalacion():
    a = None
    st.title(TITULO_REGISTRO)
    st.write(TEXTO_REGISTRO)
    caja = st.container(border=False)
    col1, col2 = st.columns(2, vertical_alignment="bottom")
    with col1:
        a = st.text_input(label="Constrasena del Administrador",type='password', label_visibility="collapsed", placeholder="Contrasena")
    with col2:
        if st.button("Guardar Contrasena del Administrador", type="primary", use_container_width=True):
            SQL_crearUsuario("ADMIN", a, cargo="ADMIN")
            caja.success("Administrador Registrado!, redirigiendo...")
            st.balloons()
            sleep(2)
            st.rerun()
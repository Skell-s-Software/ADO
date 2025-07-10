# Modulo de Chat Interno

# Importacion de Librerias
import streamlit as st
from time import sleep
from modules.database import SQL_chat_tabla, SQL_guardarMensaje, SQL_consultaGeneral

# UI del Chat Global
def CHAT():
    SQL_chat_tabla()
    mensajes_db = SQL_consultaGeneral('chat')

    # Inicializar chat en session_state si no existe
    if 'chat' not in st.session_state:
        st.session_state.chat = mensajes_db.copy()
    else:
        st.session_state.chat = mensajes_db.copy()

    with st.container(height=450, border=True):
        for mensaje in st.session_state.chat:
            st.chat_message('human').write(f'{mensaje[1]}: {mensaje[2]}')
        if prompt := st.chat_input("Escriba aqui el mensaje a enviar"):
            SQL_guardarMensaje(st.session_state.usuario, prompt)
    sleep(0.5)
    st.rerun()
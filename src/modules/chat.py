# Modulo de Chat Interno

# Importacion de Librerias
import streamlit as st
from time import sleep
from modules.database import SQL_chat_tabla, SQL_guardarMensaje, SQL_consultaGeneral

# UI del Chat Global
def CHAT():
    SQL_chat_tabla()
    st.session_state.chat = SQL_consultaGeneral('chat')
    with st.container(height=450 ,border=True):
        chat = st.session_state.chat
        for mensaje in chat:
            st.chat_message('human').write(f'{mensaje[1]}: {mensaje[2]}')
        if prompt := st.chat_input("Escriba aqui el mensaje a enviar"):
            st.session_state.chat.append(prompt)
            SQL_guardarMensaje(st.session_state.usuario, prompt)
            st.rerun()
    sleep(0.5)
    st.rerun()
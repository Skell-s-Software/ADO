# Modulo para el Punto de Venta

# Importacion de Librerias
import streamlit as st
import pandas as pd

# Importacion de Modulos
from modules.database import SQL_consultaFila

# Interfaz de Realizar Venta
def VENventas():
    cedula = st.text_input(
            "Cédula del Cliente",
            autocomplete="off",
            placeholder="Cédula del Cliente. Ej: 32942787",
            icon=":material/id_card:",
        )
    if cedula != "":
        st.session_state.clienteVenta = SQL_consultaFila(cedula, 'cedula', 'clientes')
        if st.session_state.clienteVenta:
            with st.container(border=True):
                st.subheader("Datos del Cliente")
                col1A, col1B = st.columns(2, vertical_alignment='bottom')
                with col1A:
                    st.text_input(
                        "Nombre del Cliente",
                        value=st.session_state.clienteVenta[3],
                        disabled=True
                    )
                with col1B:
                    st.text_input(
                        "Teléfono del Cliente",
                        value=st.session_state.clienteVenta[4],
                        disabled=True
                    )
            with st.container(border=True):
                st.subheader("Productos Disponibles")
                col1, col2, col3 = st.columns(3, vertical_alignment='bottom')
                col4, col5, col6 = st.columns(3, vertical_alignment='bottom')
                with col1:
                    productos = st.selectbox(
                        "Seleccionar Producto",
                        options=['Producto 1', 'Producto 2'],
                        key='producto'
                    )
                with col2:
                    cantidad = st.number_input(
                    "Cantidad a Vender",
                    min_value=1,
                    max_value=100,
                    value=1,
                    step=1, key='cantidad'
                )
                with col3:
                    agregar = st.button("Agregar Producto", type="primary", use_container_width=True)
                with col4:
                    productoE = st.selectbox(
                        "Seleccionar Producto",
                        options=['Producto 1', 'Producto 2'],
                        key='productoE'
                    )
                with col5:
                    cantidad = st.number_input(
                    "Cantidad a Manipular",
                    min_value=1,
                    max_value=100,
                    value=1,
                    step=1, key='cantidadE'
                )
                with col6:
                    manipular = st.button("Manipular Producto", type="primary", use_container_width=True)
                if agregar:
                    pass
                if manipular:
                    pass
                st.dataframe(
                    None,
                    use_container_width = True,
                    hide_index = True,
                )
        else:
            st.error("La Cédula es muy corta")
    else:
        st.warning("Escriba la cédula del cliente para poder realizar una venta, debe ser una cédula válida")
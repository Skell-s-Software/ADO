# Modulo para el Punto de Venta

# Importacion de Librerias
import streamlit as st
import pandas as pd

# Importacion de Modulos
from modules.database import SQL_consultaFila, SQL_listadoProductos

# Interfaz de Realizar Venta
def VENventas():
    cedula = st.text_input(
            "Cédula del Cliente",
            autocomplete="off",
            placeholder="Cédula del Cliente. Ej: 32942787",
            icon=":material/id_card:",
        )
    if cedula == "" and 'listaDeCompra' in st.session_state: del st.session_state.listaDeCompra
    if cedula != "":
        st.session_state.clienteVenta = SQL_consultaFila(cedula, 'cedula', 'clientes')
        if st.session_state.clienteVenta:
            # Este fragmento se encarga de construir la lista de productos disponibles
            st.session_state.listadoProductos = SQL_listadoProductos()
            listadoProductos = []
            listaDeCompra = []
            for producto in st.session_state.listadoProductos:
                listadoProductos.append(f"[{producto[1]}] - {producto[2]} ${producto[4]} Stock: {int(float(producto[5]))}")
            # Fin de construccion de lista de productos disponibles
            # Genera la lista de compra si no esta creada
            if 'listaDeCompra' not in st.session_state:
                st.session_state.listaDeCompra = []
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
                col4, col5 = st.columns(2, vertical_alignment='bottom')
                with col1:
                    productos = st.selectbox(
                        "Seleccionar Producto",
                        options=listadoProductos,
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
                    if agregar:
                        codigoProducto = int(productos.split("[")[1].split("]")[0])
                        listaDeCompra = [codigoProducto, st.session_state.listadoProductos[codigoProducto - 1][2], f"${st.session_state.listadoProductos[codigoProducto - 1][4]}", cantidad, f"${float(st.session_state.listadoProductos[codigoProducto - 1][4]) * cantidad}"]
                        if listaDeCompra not in st.session_state.listaDeCompra:
                            st.session_state.listaDeCompra.append(listaDeCompra)
                with col4:
                    productoE = st.selectbox(
                        "Seleccionar Producto",
                        options=listadoProductos,
                        key='productoE'
                    )
                with col5:
                    manipular = st.button("Eliminar Producto de Lista", type="primary", use_container_width=True)
                    if manipular:
                        codigoProducto = int(productoE.split("[")[1].split("]")[0])
                        listaDeCompra = [codigoProducto, st.session_state.listadoProductos[codigoProducto - 1][2], f"${st.session_state.listadoProductos[codigoProducto - 1][4]}", cantidad, f"${float(st.session_state.listadoProductos[codigoProducto - 1][4]) * cantidad}"]
                        if listaDeCompra in st.session_state.listaDeCompra:
                            st.session_state.listaDeCompra.pop(st.session_state.listaDeCompra.index(listaDeCompra))
                tablaCompra = pd.DataFrame(
                    st.session_state.listaDeCompra,
                    columns=["Codigo", "Nombre", "Precio", "Cantidad", "Total"]
                )
                st.subheader("Lista de Productos a Comprar")
                st.dataframe(
                    tablaCompra,
                    use_container_width = True,
                    hide_index = True,
                )
            with st.container(border=True):
                st.title("Metodo de Pago")
                totalProductos = 0
                precioBase = 0
                for producto in st.session_state.listaDeCompra:
                    precioBase += float(producto[4].split("$")[1])
                    totalProductos += int(float(producto[3]))
                st.subheader(f"Cantidad de Productos: {totalProductos}")
                st.subheader(f"Precio Total a Pagar: ${precioBase}")
        else:
            st.error("La Cédula es muy corta")
    else:
        st.warning("Escriba la cédula del cliente para poder realizar una venta, debe ser una cédula válida")
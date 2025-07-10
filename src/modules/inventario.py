# Modulo de Gestion de Inventario

# Importacion de Librerias
import streamlit as st
import pandas as pd
import io
from time import sleep

# Interfaz de Registro de Producto
def INVregistro():
    with st.form("registro", clear_on_submit = True, enter_to_submit = False):
        # Cedula del Cliente
        codigo = st.text_input(
            "Código del Producto (obligatorio)",
            help = "Ingrese aqui el código del producto a registrar.",
            placeholder = "Ej: 123",
            icon = ":material/barcode_scanner:"
        )
        # Nombre completo del Cliente a Registrar
        nombre = st.text_input(
            "Nombre del Producto (obligatorio)",
            help = "Ingrese aqui el nombre completo del producto a registrar.",
            placeholder = "Ej: Zapatillas Deportivas",
            icon = ":material/sell:"
        )
        # Numero Telefonioco del Cliente dentro del Sistema
        precio = st.number_input(
            "Precio (obligatorio)",
            help = "Ingrese aqui el precio del producto. (Los decimales se expresan con ',')",
            placeholder = "Ej: 30,00 (Los decimales se expresan con ',')",
            icon = ":material/attach_money:"
        )
        # Ubicacion o Direccion del Cliente
        proveedor = st.text_input(
            "Proveedor del Producto",
            help = "Ingrese aqui el nombre del proveedor del producto a registrar.",
            placeholder = "Ej: Nombre del Proveedor // Tienda",
            icon = ":material/store:"
        )
        # Breve Descripcion del Cliente
        descripcion = st.text_area(
            "Breve Descripcion del Producto",
            max_chars = 250,
            help = "Escriba aqui informacion complementaria a cerca del Producto.",
            placeholder = "Este producto es de alta calidad y durabilidad, ideal para deportes al aire libre.",
        )
        # Boton de Submit para registrar al Cliente
        boton = st.form_submit_button(
            "Registrar Producto",
            help = 'Al presionar este boton, se registrara el producto si los datos ingresados son validos.',
            type = 'primary',
            use_container_width = True,
            icon = ':material/box_add:'
        )

# Interfaz de Listado de Productos
def INVlista():
    tabla = pd.DataFrame(
        None,
        columns = ['Codigo', 'Stack', 'Nombre', 'Proveedor', 'Descripcion', 'Precio']
    )
    # Mostrar Tabla de Productos
    st.dataframe(
        tabla,
        use_container_width = True,
        hide_index = True,
    )

# Interfaz de Edicion de Producto
def INVeditar():
    with st.form("buscar", border = False):
        # Codigo del Producto a buscar
        codigo = st.text_input(
                "Codigo del Producto a Editar",
                help = "Ingrese aqui el codigo del producto a editar.",
                placeholder = "Ej: 123",
                icon = ":material/barcode_scanner:",
                key = "codigo",
        )
        # Boton para buscar el cliente a editar
        boton = st.form_submit_button(
            "Buscar Producto para editarlo",
            help = "Al presionar este boton el sistema buscara el codigo del producto en la base para su edicion.",
            use_container_width = True,
            type = 'primary',
            icon = ':material/search:'
        )
    botonEliminar = st.button(
        "Eliminar Producto de la Base",
        help = "Al presionar este boton el sistema buscara la codigo del producto en la base para su eliminacion.",
        use_container_width = True,
        type = 'secondary',
        icon = ':material/delete:'
    )
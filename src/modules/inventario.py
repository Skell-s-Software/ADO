# Modulo de Gestion de Inventario

# Importacion de Librerias
import streamlit as st
import pandas as pd
import io
from time import sleep

# Importacion de Modulos
from modules.database import SQL_productos_tabla, SQL_crearProducto, SQL_consultaGeneral, SQL_consultaFila, SQL_consultaEspecifica, SQL_edicionEspecifica, SQL_listadoProductos

# Interfaz de Registro de Producto
def INVregistro():
    SQL_productos_tabla()
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
        # Breve Descripcion del Cliente
        descripcion = st.text_area(
            "Breve Descripcion del Producto",
            max_chars = 250,
            help = "Escriba aqui informacion complementaria a cerca del Producto.",
            placeholder = "Este producto es de alta calidad y durabilidad, ideal para deportes al aire libre.",
        )
        # Numero Telefonioco del Cliente dentro del Sistema
        precio = st.number_input(
            "Precio (obligatorio)",
            help = "Ingrese aqui el precio del producto. (Los decimales se expresan con ',')",
            placeholder = "Ej: 30,00 (Los decimales se expresan con ',')",
            icon = ":material/attach_money:"
        )
        # Boton de Submit para registrar al Cliente
        boton = st.form_submit_button(
            "Registrar Producto",
            help = 'Al presionar este boton, se registrara el producto si los datos ingresados son validos.',
            type = 'primary',
            use_container_width = True,
            icon = ':material/box_add:'
        )
        if boton:
            if codigo and precio and nombre:
                SQL_crearProducto(codigo, nombre, precio, descripcion)
                st.success("¡Cliente registrado exitosamente!")
            else:
                st.error("¡Faltan datos por llenar!")

# Interfaz de Listado de Productos
def INVlista():
    SQL_productos_tabla()
    datos = SQL_listadoProductos()
    print(datos)
    tabla = pd.DataFrame(
        datos,
        columns = ['Codigo', 'Nombre', 'Precio', 'Descripcion', 'stack']
    )
    # Mostrar Tabla de Productos
    st.dataframe(
        tabla,
        use_container_width = True,
        hide_index = True,
    )
    # Sistema de descarga de tabla de excel
    output = io.BytesIO()
    try:
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            tabla.to_excel(writer, index=False, sheet_name='Lista')
        excel_data = output.getvalue()
        st.download_button(
            label="Descargar Listado de Productos como Archivo de Excel",
            data=excel_data,
            file_name="Listado_de_Productos.xlsx",
            use_container_width= True,
            type = 'primary',
            icon = ':material/save:'
        )
    except Exception as e:
        st.error(f"Ocurrió un error al preparar el archivo Excel para descarga: {e}")
        st.write("Asegúrate de tener `openpyxl` instalado (`pip install openpyxl`)")

# Interfaz de Edicion de Producto
def INVeditar():
    SQL_productos_tabla()
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
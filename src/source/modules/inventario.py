# Modulo de Gestion de Inventario

# Importacion de Librerias
import streamlit as st
import pandas as pd
import io
from time import sleep

# Importacion de Modulos
from modules.database import SQL_productos_tabla, SQL_crearProducto, SQL_listadoProductos, SQL_buscarProductoPorCodigo, SQL_ProductoEdicion

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
                st.success("¡Producto registrado exitosamente!")
            else:
                st.error("¡Faltan datos por llenar!")

# Interfaz de Listado de Productos
def INVlista():
    SQL_productos_tabla()
    datos = SQL_listadoProductos()
    tabla = pd.DataFrame(
        datos,
        columns = ['id', 'Codigo', 'Nombre', 'Descripcion', 'Precio', 'Stack']
    )
    # Mostrar Tabla de Productos
    st.dataframe(
        tabla[['Codigo', 'Nombre', 'Descripcion', 'Precio', 'Stack']],
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
        if boton:
            if codigo:
                producto = SQL_buscarProductoPorCodigo(codigo)
                if producto:
                    st.session_state.productoEdicion = producto
            else:
                st.warning("Ingrese un codigo valido")
    if 'productoEdicion' in st.session_state and st.session_state.productoEdicion and codigo:
        datos = [st.session_state.productoEdicion]
        tabla = pd.DataFrame(
            datos,
            columns = ['id', 'Codigo', 'Nombre', 'Descripcion', 'Precio', 'Stack']
        )
        # Mostrar Tabla de Productos
        st.dataframe(
            tabla[['Codigo', 'Nombre', 'Descripcion', 'Precio', 'Stack']],
            use_container_width = True,
            hide_index = True,
        )
        # Formulario de Edicion
        with st.form("editar", clear_on_submit = True, enter_to_submit = False):
            col1, col2 = st.columns(2, vertical_alignment='bottom')
            with col1:
                seleccion = st.selectbox(
                    "Dato a modificar",
                    [
                        'Nombre',
                        'Descripcion',
                        'Precio'
                    ],
                    help = "Seleccione el campo que modificara del Producto",
                    accept_new_options = False,
                )
            with col2:
                dato = st.text_input(
                    "Modificacion",
                    help = "Escriba aqui la Modificado",
                    placeholder = "Dato Modificado",
                    icon = ':material/edit:'
                )
            boton = st.form_submit_button(
                "Actualizar dato del Producto",
                help = "Al presinar este boton, se editara la informacion actual del producto con la informacion proporcionada por usted.",
                icon = ':material/edit:',
                type = 'primary',
                use_container_width = True
            )
            if boton:
                if dato:
                    SQL_ProductoEdicion(seleccion, dato, codigo)
                    st.success("Edicion exitosa")
                    sleep(1)
                    st.session_state.productoEdicion = SQL_buscarProductoPorCodigo(codigo)
                    st.rerun()
        # Formulario para manejar el stack
        with st.form("stack", clear_on_submit = True, enter_to_submit = False):
            col1, col2 = st.columns(2, vertical_alignment='bottom')
            with col1:
                seleccion = st.selectbox(
                    "Accion a Realizar",
                    [
                        'Sumar',
                        'Restar',
                    ],
                    help = "Seleccione el campo que modificara del Producto",
                    accept_new_options = False,
                )
            with col2:
                dato = st.number_input(
                    "Valor",
                    help = "Escriba aqui la el valor",
                    placeholder = "Ej: 10",
                    icon = ':material/edit:',
                    min_value = 1,
                    step = 1
                )
            boton = st.form_submit_button(
                "Actualizar Stock",
                help = "Al presinar este boton, se editara la informacion actual del producto con la informacion proporcionada por usted.",
                icon = ':material/edit:',
                type = 'primary',
                use_container_width = True
            )
            if boton:
                if dato:
                    cantidad = dato if seleccion == "Sumar" else -dato
                    SQL_ProductoEdicion('stack', cantidad, codigo)
                    st.success("Edicion exitosa")
                    sleep(1)
                    st.session_state.productoEdicion = SQL_buscarProductoPorCodigo(codigo)
                    st.rerun()
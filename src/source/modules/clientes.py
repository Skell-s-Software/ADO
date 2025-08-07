# Modulo de Gestor de Clientes

# Importacion de Librerias
import streamlit as st
import pandas as pd
import io
from time import sleep

# Importacion de modulos
from modules.database import SQL_clientes_tabla, SQL_consultaGeneral, SQL_crearCliente, SQL_consultaFila, SQL_ClientedicionEspecifica

# Interfaz de Registro del Cliente en el Sistema
def CRegistro():
    SQL_clientes_tabla()
    with st.form("registro", clear_on_submit = True, enter_to_submit = False):
        # Cedula del Cliente
        cedula = st.text_input(
            "C.I. del Cliente (obligatorio)",
            help = "Ingrese aqui la cedula de identidad del cliente a registrar.",
            placeholder = "Ej: 12345786",
            icon = ":material/id_card:"
        )
        # Codigo del Socio dentro del Sistema
        codigoSocio = st.text_input(
            "Codigo de Socio",
            help = "Ingrese aqui el codigo de socio del cliente a registrar. Si el numero ya esta ocupado, el sistema le avisara y le proporcionara los numeros disponibles. En caso de no agregar el codigo de socio desde el principio del registro, podra agregarlo posteriormente en la edicion.",
            placeholder = "Ej: 1234",
            icon = ":material/badge:"
        )
        # Nombre completo del Cliente a Registrar
        nombre = st.text_input(
            "Nombre del Cliente (obligatorio)",
            help = "Ingrese aqui el nombre completo del cliente a registrar.",
            placeholder = "Ej: Nombre Nombre2 Apellido Apellido2",
            icon = ":material/person:"
        )
        # Numero Telefonioco del Cliente dentro del Sistema
        telefono = st.text_input(
            "Numero Telefonico del Cliente (obligatorio)",
            help = "Ingrese aqui el numero telefonico del cliente",
            placeholder = "Ej: 0426-4572138",
            icon = ":material/phone:"
        )
        # Correo Electronico del Cliente a Registrar
        correo = st.text_input(
            "Correo Electronico del Cliente",
            help = "Ingrese aqui el correo electronico del cliente a registrar.",
            placeholder = "Ej: ejemplo@email.com",
            icon = ":material/email:"
        )
        # Ubicacion o Direccion del Cliente
        direccion = st.text_input(
            "Direccion del Cliente",
            help = "Ingrese aqui la direccion del cliente a registrar.",
            placeholder = "Ej: Carrera 16 Entre Calle 40 y 41",
            icon = ":material/pin_drop:"
        )
        # Breve Descripcion del Cliente
        descripcion = st.text_area(
            "Breve Descripcion del Cliente",
            max_chars = 250,
            help = "Escriba aqui informacion complementaria a cerca del cliente.",
            placeholder = "Este cliente es el creador de Skell's CRM"
        )
        # Boton de Submit para registrar al Cliente
        boton = st.form_submit_button(
            "Registrar Cliente",
            help = 'Al presionar este boton, se registrara el cliente si los datos ingresados son validos.',
            type = 'primary',
            use_container_width = True,
            icon = ':material/person_add:'
        )
        if boton:
            if cedula and codigoSocio and nombre and telefono:
                if len(cedula) > 6 and len(telefono) > 10:
                    SQL_crearCliente(cedula, nombre, telefono, correo, direccion, descripcion, codigoSocio)
                    st.success("¡Cliente registrado exitosamente!")
                else:
                    st.error("¡Los datos ingresados no son validos!")
            else:
                st.error("¡Faltan datos por llenar!")

# Interfaz de Listado de Clientes en el Sistema
def CListado():
    SQL_clientes_tabla()
    datos = SQL_consultaGeneral('clientes') 
    tabla = pd.DataFrame(
        datos,
        columns = ['id', 'Cedula', 'Codigo Socio', 'Nombre', 'Telefono', 'Correo', 'Direccion', 'Descripcion']
    )
    # Mostrar Tabla de Clientes
    st.dataframe(
        tabla[['Cedula', 'Codigo Socio', 'Nombre', 'Telefono', 'Correo', 'Direccion', 'Descripcion']],
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
            label="Descargar Listado de Clientes como Archivo de Excel",
            data=excel_data,
            file_name="Listado_de_Clientes.xlsx",
            use_container_width= True,
            type = 'primary',
            icon = ':material/save:'
        )
    except Exception as e:
        st.error(f"Ocurrió un error al preparar el archivo Excel para descarga: {e}")
        st.write("Asegúrate de tener `openpyxl` instalado (`pip install openpyxl`)")

# Interfaz de Edicion de Clientes en el Sistema
def CEdicion():
    SQL_clientes_tabla()
    with st.form("buscar", border = False):
        # Cedula del Cliente a buscar
        cedula = st.text_input(
                "Cedula de Identidad (C.I.) del Cliente a Editar",
                help = "Ingrese aqui la cedula de identidad del cliente a editar.",
                placeholder = "Ej: 12345786",
                icon = ":material/id_card:",
                key = "cliente",
        )
        # Boton para buscar el cliente a editar
        boton = st.form_submit_button(
            "Buscar cliente para editarlo",
            help = "Al presionar este boton el sistema buscara la cedula del cliente en la base para su edicion.",
            use_container_width = True,
            type = 'primary',
            icon = ':material/search:'
        )
        if boton:
            if cedula:
                cliente = SQL_consultaFila(cedula, 'cedula', 'clientes')
                if cliente:
                    st.session_state.clienteEdicion = cliente
            else:
                st.warning("Ingrese una cedula valida")
    if 'clienteEdicion' in st.session_state and st.session_state.clienteEdicion and cedula:
        datos = [st.session_state.clienteEdicion]
        tabla = pd.DataFrame(
            datos,
            columns = ['id', 'Cedula', 'Codigo Socio', 'Nombre', 'Telefono', 'Correo', 'Direccion', 'Descripcion']
        )
        st.dataframe(
            tabla[['Cedula', 'Codigo Socio', 'Nombre', 'Telefono', 'Correo', 'Direccion', 'Descripcion']],
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
                        'Cedula',
                        'Codigo Socio',
                        'Nombre',
                        'Telefono',
                        'Correo',
                        'Direccion',
                        'Descripcion'
                    ],
                    help = "Seleccione el campo que modificara del Cliente",
                    accept_new_options = False,
                )
            with col2:
                dato = st.text_input(
                    "Modificacion",
                    help = "Escriba aqui la Modificacion",
                    placeholder = "Dato Modificado",
                    icon = ':material/edit:'
                )
            boton = st.form_submit_button(
                "Actualizar dato del Cliente",
                help = "Al presinar este boton, se editara la informacion actual del cliente con la informacion proporcionada por usted.",
                icon = ':material/edit:',
                type = 'primary',
                use_container_width = True
            )
            if boton:
                if dato:
                    SQL_ClientedicionEspecifica(seleccion, dato, cedula)
                    st.success("Edicion exitosa")
                    sleep(1)
                    st.session_state.clienteEdicion = SQL_consultaFila(cedula, 'cedula', 'clientes')
                    st.rerun()

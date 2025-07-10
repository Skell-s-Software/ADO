# Modulo de Gestor de Clientes

# Importacion de Librerias
import streamlit as st
import pandas as pd
import io
from time import sleep

# Interfaz de Registro del Cliente en el Sistema
def CRegistro():
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

# Interfaz de Listado de Clientes en el Sistema
def CListado():
    tabla = pd.DataFrame(
        None,
        columns = ['Cedula', 'Codigo Socio', 'Nombre', 'Telefono', 'Correo', 'Direccion', 'Descripcion']
    )
    # Mostrar Tabla de Clientes
    st.dataframe(
        tabla,
        use_container_width = True,
        hide_index = True,
    )

# Interfaz de Edicion de Clientes en el Sistema
def CEdicion():
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
    botonEliminar = st.button(
        "Eliminar Cliente de la Base",
        help = "Al presionar este boton el sistema buscara la cedula del cliente en la base para su edicion.",
        use_container_width = True,
        type = 'secondary',
        icon = ':material/delete:'
    )
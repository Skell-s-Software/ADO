# Modulo Principal

# Importacion de Librerias
import streamlit as st

# Importacion de Constantes
from constantes import TITULO_PAGINA
from constantes import ICONO_PAGINA
from constantes import BASE_DATOS
from constantes import SIDEBAR_VARIANTES

# Importacion de Modulos
from streamlit_option_menu import option_menu as stmenu
from modules.database import SQL_server_tabla, SQL_consultaEspecifica, SQL_consultaGeneral, SQL_usuarios_tabla
from modules.register import pagina_instalacion
from modules.login import pagina_login, dialog_logout
from modules.ayuda import pagina_ayuda
from tart import logo

# Importacion de Modulos de Funcionalidad
from modules.clientes import CRegistro, CListado, CEdicion
from modules.inventario import INVregistro, INVlista, INVeditar
from modules.ventas import VENventas#, VEN, VEN
from modules.chat import CHAT

# Funciones Internas
def configurar_sitio():
    st.set_page_config(
        page_title=TITULO_PAGINA,
        page_icon=ICONO_PAGINA,
        layout="centered"
    )
    #if 'despliegue' not in st.session_state:
    st.session_state.despliegue = verificar_instalacion()
def verificar_instalacion():
    # Verificar si la base de datos existe y si la tabla 'server' tiene al menos un despliegue
    SQL_usuarios_tabla(BASE_DATOS)
    SQL_server_tabla(BASE_DATOS)
    # print(SQL_consultaEspecifica('despliegues', 'variable', 'server', 'valor', BASE_DATOS))
    return int(SQL_consultaEspecifica('despliegues', 'variable', 'server', 'valor', BASE_DATOS))

def main():
    logo()
    # Configuracion del Sitio
    configurar_sitio()
    # Verificar la Instalacion
    if st.session_state.despliegue == 0:
        pagina_instalacion()
    else: # En caso de que SI ESTE INSTALADO
        if 'usuario' not in st.session_state:
            with st.sidebar:
                ventana = stmenu(
                    SIDEBAR_VARIANTES["LOGIN"]["TITULO"],
                    SIDEBAR_VARIANTES["LOGIN"]["OPCIONES"],
                    icons=SIDEBAR_VARIANTES["LOGIN"]["ICONOS"]
                )
            if ventana == "Principal":
                pagina_login()
            else:
                pagina_ayuda()
        else:
            if st.session_state.cargo != None and st.session_state.usuario != None:
                with st.sidebar:
                    ventana = stmenu(
                        SIDEBAR_VARIANTES["ADO"]["TITULO"],
                        SIDEBAR_VARIANTES["ADO"]["OPCIONES"][st.session_state.cargo],
                        icons=SIDEBAR_VARIANTES["ADO"]["ICONOS"][st.session_state.cargo],
                    )
                    LOGUOT = st.button(
                        "Cerrar Sesion",
                        type = 'primary',
                        use_container_width = True,
                        icon = ':material/logout:'
                    )
                    if LOGUOT:
                        dialog_logout()
                st.write(f"Bienvenido {st.session_state.usuario}, {st.session_state.cargo}")
                TAB = None
                if ventana == "Información y Ayuda":
                    pagina_ayuda()
                    TAB = False
                if ventana == "Clientes":
                    TITULO_TAB = "Gestión de Clientes"
                    OPCIONES_TAB = ['Registrar Clientes', 'Lista de Clientes', 'Edición de Clientes']
                    TAB = True
                elif ventana == "Inventario":
                    TITULO_TAB = "Gestión de Inventario"
                    OPCIONES_TAB = ['Registrar Producto', 'Lista de Productos', 'Edición de Productos']
                    TAB = True
                elif ventana == "Ventas":
                    TITULO_TAB = "Punto de Venta"
                    OPCIONES_TAB = ['Realizar Venta', 'Historial de Ventas', 'Pagos Pendientes']
                    TAB = True
                elif ventana == "Chat Interno":
                    TAB = False
                    CHAT()
                elif ventana == "Notificaciones":
                    TAB = False
                    st.title(ventana)
                if TAB:
                    tab = stmenu(
                        TITULO_TAB,
                        OPCIONES_TAB,
                        default_index = 1,
                        menu_icon = 'people',
                        icons = ['person-add', 'person-lines-fill', 'pencil'],
                        orientation = 'horizontal'
                    )
                    if tab == "Registrar Clientes":
                        CRegistro()
                    elif tab == "Lista de Clientes":
                        CListado()
                    elif tab == "Edición de Clientes":
                        CEdicion()
                    elif tab == "Registrar Producto":
                        INVregistro()
                    elif tab == "Lista de Productos":
                        INVlista()
                    elif tab == "Edición de Productos":
                        INVeditar()
                    elif tab == "Realizar Venta":
                        VENventas()
                    elif tab == "Historial de Ventas":
                        pass
                    elif tab == "Pagos Pendientes":
                        pass

    # print(st.session_state)
# Punto de Entrada Principal
if __name__ == "__main__":
    main()
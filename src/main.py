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
    print(SQL_consultaEspecifica('despliegues', 'variable', 'server', 'valor', BASE_DATOS))
    return int(SQL_consultaEspecifica('despliegues', 'variable', 'server', 'valor', BASE_DATOS))

def main():
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
            if st.session_state.cargo == "Gestor Principal":
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
                if ventana != "Información y Ayuda":
                    st.title(ventana)
                else:
                    pagina_ayuda()
                if ventana == "Clientes":
                    pass
                elif ventana == "Inventario":
                    pass
                elif ventana == "Ventas":
                    pass
                elif ventana == "Chat Interno":
                    pass
                elif ventana == "Notificaciones":
                    pass

    print(st.session_state)
# Punto de Entrada Principal
if __name__ == "__main__":
    main()
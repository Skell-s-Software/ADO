# Modulo Principal

# Importacion de Librerias
import streamlit as st

# Importacion de Constantes
from constantes import TITULO_PAGINA
from constantes import ICONO_PAGINA
from constantes import BASE_DATOS

# Importacion de Modulos
from modules.database import SQL_server_tabla, SQL_consultaEspecifica, SQL_consultaGeneral, SQL_usuarios_tabla
from modules.register import pagina_instalacion
from modules.login import pagina_login

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
            pagina_login()
        else:
            st.write(f"Bienvenido al Sistema {st.session_state.usuario}")

    print(st.session_state)
# Punto de Entrada Principal
if __name__ == "__main__":
    main()
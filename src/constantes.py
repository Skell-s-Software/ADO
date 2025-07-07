# En este archivo estarán las constantes, como rutas, nombres de iconos, etc. que se utilizarán en el programa.

# Constantes generales del programa
TITULO_PAGINA = "Skell's ADO"
ICONO_PAGINA = "src/img/iconTemporal.ico"
BASE_DATOS = "src/database/ado.db"

# Constantes del Register.py
TITULO_REGISTRO = "Instalación de Skell's ADO"
TEXTO_REGISTRO = "Bienvenido a la instalación de ***Skell's ADO***, una herramienta para la gestión de proyectos y tareas. Es necesario que proporciones una ***contraseña*** para crear el usuario administrador. Esta contraseña se utilizará para controlar las configuraciones importantes de la aplicación. ***Te recomendamos guardarla de forma segura,*** ya que, de lo contrario, tendrás que contactar al servicio técnico para restablecerla."

# Constantes del Login.py
TITULO_LOGIN = "Inicio de Usuario"
ICONO_LOGIN = ""
ICONO2_LOGIN = ""

# Array Bidimensional con todas las variantes existentes de elementos para el SideBar
SIDEBAR_VARIANTES = {
    "LOGIN": {
        "TITULO": "Opciones",
        "OPCIONES": ["Principal", "Información y Ayuda"],
        "ICONOS": ["house", "question-circle"]
    },
    "ADO": {
        "TITULO": "Opciones",
        "OPCIONES": {
            "Gestor Principal": ["Clientes", "Inventario", "Ventas", "Chat Interno", "Notificaciones", "Información y Ayuda"],
            "Gestor de Inventario": ["Inventario", "Chat Interno", "Notificaciones", "Información y Ayuda"],
            "Punto de Venta": ["Clientes", "Ventas", "Chat Interno", "Notificaciones", "Información y Ayuda"],
            "Gestor de Clientes": ["Clientes", "Ventas", "Chat Interno", "Notificaciones", "Información y Ayuda"]
        },
        "ICONOS": {
            "Gestor Principal": ["people", "boxes", "cash-coin", "chat-left-dots", "bell", "question-circle"],
            "Gestor de Inventario": ["boxes", "chat-left-dots", "bell", "question-circle"],
            "Punto de Venta": ["people","cash-coin", "chat-left-dots", "bell", "question-circle"],
            "Gestor de Clientes": ["people", "cash-coin", "chat-left-dots", "bell", "question-circle"]
        }
    }
}
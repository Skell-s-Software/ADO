# Skell's ADO - Documentacion
> Este documento contiene toda la documentacion referente a cada modulo individual de la carpeta ../src/modules y otros archivos en el directorio raíz.
# Índice
- [OS-launch (.bat | .bash)](#os-launch-bat--bash)
- [Main (py)](#main-py)
- [Constantes (py)](#constantes-py)

# Contenido
> Todo esta informacion esta sujeta a sufrir cambios en momentos de refactorizacion e inclusive puede llegara no concordar con el estado actual del codigo.

### OS-launch (.bat | .bash)
Estos Scripts son un codigo de automatizacion de ejecucion del Skell's ADO para cada sistema operativo correspondiente

- **WINDOWS-launch.bat:** Este script esta diseñado para poder ejecutarse dentro del directorio donde se encuentren los archivos del servidor, se recomienda trasladar unicamente un acceso directo para evitar problemas de directorios o ficheros no encontrados.
```
streamlit run src/main.py --server.port 8501
```
- **LINUX-launch.bash:** Este script está diseñado unicamente para ejecutarse en distribuciones Linux, posee el mismo codigo de comando que el de Windows, la diferencia es la extension del archivo y compatibilidad.


### Main (py)

### Constantes (py)
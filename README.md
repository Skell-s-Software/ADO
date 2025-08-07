<!-- Badges (ejemplo) -->
![Python](https://img.shields.io/badge/Python-3.13.3%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.48.0-FF4B4B)
![SQLite](https://img.shields.io/badge/SQLite-3-green)
![License](https://img.shields.io/badge/License-MIT-orange)

# Skell's ADO

![Version](https://img.shields.io/badge/Version-1.0.0-blueviolet)
![Build](https://img.shields.io/badge/Build-Unknown-brightgreen)

![Logo de Skell's ADO](./img/logo.png)

Software de gestión empresarial construido en Python con Streamlit para entornos web. Permite administrar:

- Inventario.
- Clientes.
- Ventas y Estadísticas.
- Productos y Inventario.

y más, **en un solo equipo local** que funciona como servidor accesible desde cualquier dispositivo en la red.

## Características Principales

### 1. Portabilidad
***Base de datos autocontenida*** en un archivo cifrado *(SQLite3)*. No requiere servidores externos.

### 2. Velocidad Y Eficiencia
Las consultas SQL están ***optimizadas*** y la velocidad de la aplicación no depende
del hardware del servidor, solo del cliente debido a ser una ***aplicación web.***

### 3. Adaptabilidad
Puede funcionar en ***cualquier dispositivo*** sea servidor o cliente, el único requisito es la conexión a internet y apertura en la red local.

### 4. Modularidad
Se pueden agregar ***nuevos modulos*** de forma cási ***automatizada*** simplemente agregando un archivo con lo que se desea mostrar y elaborar en "./src/source/modules" ya que automaticamente ***se agregará al software.***

## Ejecución
Dentro de "./scripts" se encuentran dos archivos de comandos, ejecute el respectivo para su plataforma, Windows, Linux.

## Documentación
Toda la documentación técnica está en "./doc" separada en varios archivos por módulo.
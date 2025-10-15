# PeticionGet - Consumo de API con Python

Script simple en Python para realizar peticiones GET a una API REST y procesar los datos recibidos.

## Descripción

Aplicación que consume la API de JSONPlaceholder para obtener posts, mostrar los primeros 5 títulos en consola y guardar los datos en una estructura de datos local.

## Tecnologías

Python 3.x | requests library | REST API

## Estructura del Proyecto

    PeticionGet.py

## Instalación

### 1. Instalar dependencias

    pip install requests

### 2. Ejecutar

    python PeticionGet.py

## Funcionalidad

El script realiza lo siguiente:

1. Realiza petición GET a https://jsonplaceholder.typicode.com/posts
2. Verifica que la respuesta sea exitosa (código 200)
3. Convierte la respuesta JSON en datos de Python
4. Muestra los títulos de los primeros 5 posts
5. Guarda los datos en una lista de diccionarios

## Ejemplo de Salida

    Titulos de los primeros 5 post:
    - sunt aut facere repellat provident occaecati excepturi optio reprehenderit
    - qui est esse
    - ea molestias quasi exercitationem repellat qui ipsa sit aut
    - eum et est occaecati
    - nesciunt quas odio

    Datos guardados correctamente en la lista

## Código Principal

    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for post in data[:5]:
            print(f"- {post['title']}")
        post = data[:5]

## API Utilizada

JSONPlaceholder - API REST de prueba gratuita
Endpoint: https://jsonplaceholder.typicode.com/posts

## Información del Desarrollador

Nombre: SebitasDown
GitHub: @SebitasDown

## Licencia

Proyecto educativo - Código abierto

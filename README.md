# 🚀 API Requests Python - Colección de Scripts

Colección de scripts en Python para consumir APIs REST con diferentes tipos de peticiones HTTP (GET, POST) y manejo de parámetros.

## 📋 Descripción

Proyecto educativo que demuestra cómo realizar peticiones HTTP a APIs REST utilizando la librería `requests` de Python. Incluye ejemplos prácticos de peticiones GET, POST y uso de parámetros de consulta.

## 🛠️ Tecnologías

- **Python 3.x** 🐍
- **requests** (Librería HTTP)
- **JSONPlaceholder API** (API de prueba)

## 📂 Estructura del Proyecto

    📦 api-requests-python/
    ├── 📄 PeticionGet.py
    ├── 📄 PeticionPOST.py
    └── 📄 PeticionesConParametros.py

## ⚙️ Instalación

### 1️⃣ Instalar dependencias

    pip install requests

### 2️⃣ Ejecutar scripts

    python PeticionGet.py
    python PeticionPOST.py
    python PeticionesConParametros.py

## 📝 Scripts Incluidos

### 🔍 PeticionGet.py

Realiza una petición GET a la API de JSONPlaceholder para obtener posts.

**Funcionalidad:**
- ✅ Obtiene lista de posts
- ✅ Muestra los primeros 5 títulos
- ✅ Guarda datos en lista de diccionarios
- ✅ Manejo de errores con códigos de estado

**Ejemplo de salida:**

    Titulos de los primeros 5 post:
    - sunt aut facere repellat provident occaecati excepturi optio reprehenderit
    - qui est esse
    - ea molestias quasi exercitationem repellat qui ipsa sit aut
    - eum et est occaecati
    - nesciunt quas odio
    
    Datos guardados correctamente en la lista

### ✏️ PeticionPOST.py

Crea nuevos posts mediante peticiones POST con datos ingresados por el usuario.

**Funcionalidad:**
- ✅ Solicita título y texto al usuario
- ✅ Genera ID automático con `itertools.count`
- ✅ Envía petición POST con formato JSON
- ✅ Muestra respuesta del servidor
- ✅ Validación de código 201 (Created)

**Ejemplo de uso:**

    Ingresa el titulo para el post: Mi primer post
    Ingresa el texto: Este es el contenido de mi post
    
    Se ha creado correctamente el post
    Respuesta del servidor:
    {'title': 'Mi primer post', 'body': 'Este es el contenido...', 'userId': 1, 'id': 101}

### 🔎 PeticionesConParametros.py

Consulta comentarios de un post específico usando parámetros de URL.

**Funcionalidad:**
- ✅ Solicita ID del post al usuario
- ✅ Envía parámetros en la petición GET
- ✅ Lista todos los emails de los comentarios
- ✅ Muestra código de estado HTTP

**Ejemplo de uso:**

    Ingresa el id para saber los correos de ese post: 1
    
    Codigo de estado 200
    
    Emails de los comentarios del post 1:
    
    Eliseo@gardner.biz
    Jayne_Kuhic@sydney.com
    Nikita@garfield.biz
    Lew@alysha.tv
    Hayden@althea.biz

## 🎯 Características Clave

- 🌐 **Consumo de API REST** - Peticiones HTTP profesionales
- 📊 **Procesamiento JSON** - Conversión y manejo de datos
- 🔄 **Autoincremento de IDs** - Generación automática con itertools
- ✅ **Validación de Respuestas** - Manejo de códigos HTTP
- 📝 **Interacción con Usuario** - Entrada de datos por consola
- 🎨 **Formato de Salida** - Presentación clara de resultados

## 📚 Conceptos Aplicados

### Métodos HTTP

- **GET** - Obtener datos del servidor
- **POST** - Enviar datos al servidor

### Códigos de Estado HTTP

- **200 OK** - Petición exitosa
- **201 Created** - Recurso creado correctamente
- **4xx/5xx** - Errores de cliente/servidor

### Manejo de Parámetros

    params = {"postId": 1}
    response = requests.get(url, params=params)

## 🌐 API Utilizada

**JSONPlaceholder** - API REST de prueba gratuita

- 📍 Base URL: `https://jsonplaceholder.typicode.com`
- 📝 Endpoints:
  - `/posts` - Lista de posts
  - `/comments` - Lista de comentarios

## 💡 Ejemplos de Código

### Petición GET Simple

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)

### Petición POST con JSON

    nuevo_post = {"title": "Título", "body": "Contenido", "userId": 1}
    response = requests.post(url, json=nuevo_post)
    if response.status_code == 201:
        print("Creado exitosamente")

### Petición con Parámetros

    params = {"postId": 1}
    response = requests.get(url, params=params)
    data = response.json()

## 🚀 Mejoras Futuras

- [ ] Agregar peticiones PUT y DELETE
- [ ] Implementar manejo de excepciones avanzado
- [ ] Agregar headers personalizados
- [ ] Guardar respuestas en archivos JSON
- [ ] Crear interfaz gráfica con tkinter
- [ ] Agregar autenticación con tokens
- [ ] Implementar logging de peticiones

## 👨‍💻 Información del Desarrollador

**Nombre:** SebitasDown  
**GitHub:** @SebitasDown  
**Proyecto:** API Requests Python Collection

## 📄 Licencia

Proyecto educativo - Código abierto para aprendizaje

---

**Desarrollado con 💙 Python y ☕ muchas peticiones HTTP**

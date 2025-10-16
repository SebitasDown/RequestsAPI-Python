import requests

# Importacion para que se auto genere el id cada ves que se haga un post

from itertools import count

# Generador autoincrementañ de IDs
id_generator = count(1)

# Url de la API

url = "https://jsonplaceholder.typicode.com/posts"

# Datos que se le piden al usuario

titulo = input ("Ingresa el titulo para el post: ")
texto = input ("Ingresa el texto: ")
userId = next(id_generator) # autoincrementa cada vez

# Datos para enviar formato JSON

nuevoPost = {
    "title": titulo,
    "body" :texto,
    "userId" : userId
}

# Hacemos la peticion post
response = requests.post(url, json=nuevoPost)

if response.status_code == 201:
    print("Se ha creado correctamente el post")
    print("Respuesta del servidor")
    print(response.json())
else:
    print("Error no se pudo crear el post", response.status_code)    
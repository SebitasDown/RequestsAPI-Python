import requests;

# Url API
url = "https://jsonplaceholder.typicode.com/comments";

idPost = input("Ingresa el id para saber los correos de ese post: ")


# Parametros
parametros = {"postId":idPost}

# Hacemos la peticion GET
response = requests.get(url, params=parametros)

# Verificamos el código de estado

print("Codigo de estado", response.status_code)

# Si todo salio bien osea que el status_code es 200, procesamos la respuesta

if response.status_code == 200:
    data = response.json()

    print("\n Emails de los cometarios del post 1: \n")

    for comment in data:
        print(comment["email"])

else:
    print("Error en la peticion. Codigo:", response.status_code)       
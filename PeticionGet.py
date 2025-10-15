import requests;
# Vamos a guardar la Url en una variable
url = "https://jsonplaceholder.typicode.com/posts";

# Realizamos la peticion GET a la API
response = requests.get(url);

# Verificamos que la peticion sea exitosa

if response.status_code == 200:

    data = response.json()

    print("Titulos de los primeros 5 post:")
    for post in data[:5]:
        print(f"- {post['title']}")



    # Guardamos los datos en una lista de diccionarios 
    post = data[:5]
    print("\n Datos gurdados correctamente en la lista")

else:
    print(f"Errir en la petición: {response.status_code}")
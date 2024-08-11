import os
import requests

# recupera el valor del secreto "ACCESS_TOKEN" del repositorio
token = os.environ.get("ACCESS_TOKEN")

# haz una solicitud a la API de GitHub para obtener la información de la última versión
url = "https://api.github.com/repos/tu_usuario/tu_repositorio/releases/latest"
headers = {"Authorization": f"Token {token}"}
response = requests.get(url, headers=headers)

# verifica si la solicitud fue exitosa
if response.status_code == 200:
    # extrae la información de la última versión
    data = response.json()
    tag_name = data["tag_name"]
    print(f"La última versión de tu repositorio es: {tag_name}")
else:
    print("Error al obtener la última versión del repositorio.")


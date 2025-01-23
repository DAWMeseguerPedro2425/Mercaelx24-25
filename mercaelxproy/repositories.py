import requests
import os
#from requests.auth import HTTPBasicAuth


#----UD10.1.a----
# Token de autenticación de GitHub
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

if not GITHUB_TOKEN:
    raise ValueError("El token de GitHub no está definido en la variable de entorno GITHUB_TOKEN")

url = 'https://api.github.com/search/repositories' # endpoint de la API de GitHub


# Cabeceras de la petición
headers = {
    'Authorization': f'Bearer {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'

}
# Parámetros de búsqueda
params = {
    'q': 'language:Python stars:>5000',
    'sort': 'stars',
    'order': 'desc'
}



# Request a la API de GitHub
responsegithub = requests.get(url, params=params, headers=headers)

if responsegithub.status_code == 200:
    data = responsegithub.json()
    print(f"Total de repositorios encontrados: {data['total_count']}") # Total de repositorios encontrados
    for repo in data['items']:
        print(f"Nombre: {repo['name']}, Estrellas: {repo['stargazers_count']}, URL: {repo['html_url']}") # Nombre, estrellas y URL del repositorio
else:
    print(f"Error: {responsegithub.status_code}")
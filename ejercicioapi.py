from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import requests

#Api obtiene numero
response = requests.get("http://www.randomnumberapi.com/api/v1.0/random?min=100&max=999&count=1")
random = str(response.json())
nombrearchivo = random[1:4] + ".txt"
textoarchivo = "1084120 y 1070720"

#Crear Archivo
archivo = open(nombrearchivo, "w")
archivo.write(textoarchivo)
archivo.close()

#Api subir archivo
CLIENT_SECRET_FILE = "cliente.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

folder_id = "1VHCIaecXjfombOJpoPq7PeqLk_hTkDu7"
file_names = [nombrearchivo]
mime_types = ["text/plain"]

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
        "name" : file_name,
        "parents" : [folder_id]
    }
    media = MediaFileUpload("./{0}".format(file_name), mimetype=mime_type)
    service.files().create(
        body=file_metadata,
        media_body = media,
        fields = "id"
    ).execute()

#Referencias de Conexion de Api de Google
    #https://tecnonovax.wordpress.com/subir-archivos-al-drive-con-python/
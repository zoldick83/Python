#esta es la libreria que permite cargar el archivo .env que contiene 
#las variables de entorno
from dotenv import load_dotenv
import os

load_dotenv()
variable1 = os.getenv("ALEXIS")
print(variable1)

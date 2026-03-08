import os
from dotenv import load_dotenv
from roboflow import Roboflow

# 1. Carrega as variáveis de segurança do arquivo .env
load_dotenv()

# 2. Puxa a chave de forma segura
API_KEY = os.getenv("ROBOFLOW_API_KEY")

# 3. Faz o download do dataset
rf = Roboflow(api_key=API_KEY)
project = rf.workspace("robotdog-5oy4l").project("my-first-project-vluen")
version = project.version(4)

# O dataset será baixado e extraído para a pasta atual
dataset = version.download("yolov8")
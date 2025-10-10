
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

ENVIRONMENT = "ENVIRONMENT"

# LexenProd
user = 'LexenProd'

# Lógica condicional para seleccionar las credenciales
if user != 'LexenProd':
    # Entorno de Desarrollo/Pruebas (el que usabas en el 'if')
    url: str = "https://zfkyqurrfqktsfbfjtsg.supabase.co"
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inpma3lxdXJyZnFrdHNmYmZqdHNnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkzNDcyMDgsImV4cCI6MjA3NDkyMzIwOH0.BnUSh942SJPKjOagPcwhVFe-X5QGMqjRKWKoyx6M3mg"
else:
    # Entorno de Producción (el que usabas en el 'else')
    url: str = "https://cksekrtsvdiwgcoodrfq.supabase.co/"
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNrc2VrcnRzdmRpd2djb29kcmZxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTk1MjM5NDEsImV4cCI6MjA3NTA5OTk0MX0.E7fdEkZn6HegoxJ0XU9D90fzOILrDEzNhtbwkipLqYo"


if not url or not key:
    raise RuntimeError("Define SUPABASE_URL y SUPABASE_KEY en el .env")

# La creación del cliente ahora funcionará
supabase_client: Client = create_client(url, key)

def debug_credentials():
    print(f"ENVIRONMENT: {ENVIRONMENT}")
    print(f"URL: {url}")
    print(f"KEY (preview): {key[:8]}...")


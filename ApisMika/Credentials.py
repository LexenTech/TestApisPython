import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

ENVIRONMENT = os.getenv("ENVIRONMENT", "test")

if ENVIRONMENT == "prod":
    url = os.getenv("SUPABASE_URL_PROD")
    key = os.getenv("SUPABASE_KEY_PROD")
else:
    url = os.getenv("SUPABASE_URL_TEST")
    key = os.getenv("SUPABASE_KEY_TEST")

if not url or not key:
    raise RuntimeError("Define las variables de entorno de Supabase correctamente")

supabase_client: Client = create_client(url, key)

def debug_credentials():
    print(f"ENVIRONMENT: {ENVIRONMENT}")
    print(f"URL: {url}")
    print(f"KEY (preview): {key[:8]}...")

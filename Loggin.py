import os
from supabase import create_client, Client
import Crud as c

# Asigna los valores directamente a las variables
url: str = "https://zfkyqurrfqktsfbfjtsg.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inpma3lxdXJyZnFrdHNmYmZqdHNnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTkzNDcyMDgsImV4cCI6MjA3NDkyMzIwOH0.BnUSh942SJPKjOagPcwhVFe-X5QGMqjRKWKoyx6M3mg"

if not url or not key:
    raise RuntimeError("Define SUPABASE_URL y SUPABASE_KEY en el .env")

# La creación del cliente ahora funcionará
supabase: Client = create_client(url, key)

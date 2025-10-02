
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Any, Dict
import Credentianls as cred   # importa tu cliente supabase desde credentials.py

app = FastAPI(title="API Usuarios - Salón")

# Habilitar CORS (ajusta los orígenes en producción)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# Models
# -------------------------
class UsuarioCreate(BaseModel):
    nombre: str
    apellidopaterno: str
    apellidomaterno: Optional[str] = None
    correo: str
    passwordhash: str
    telefono: Optional[str] = None
    rolid: int
    sucursalid: Optional[int] = None

class UsuarioUpdate(BaseModel):
    nombre: Optional[str]
    apellidopaterno: Optional[str]
    apellidomaterno: Optional[str]
    correo: Optional[str]
    passwordhash: Optional[str]
    telefono: Optional[str]
    rolid: Optional[int]
    sucursalid: Optional[int]

class PatchField(BaseModel):
    column: str
    value: Any

# -------------------------
# Helpers
# -------------------------
def handle_response(res):
    # Respuesta standard para supabase-py
    if getattr(res, "error", None):
        raise HTTPException(status_code=500, detail=str(res.error))
    return res.data

# -------------------------
# Endpoints CRUD
# -------------------------

@app.get("/usuarios")
def get_usuarios():
    try:
        res = cred.supabase.table("usuarios").select("*").execute()
        return handle_response(res)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/usuarios/{usuario_id}")
def get_usuario(usuario_id: int):
    try:
        res = cred.supabase.table("usuarios").select("*").eq("id", usuario_id).execute()
        data = handle_response(res)
        if not data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return data[0]
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/usuarios", status_code=201)
def create_usuario(u: UsuarioCreate):
    try:
        payload = u.dict()
        res = cred.supabase.table("usuarios").insert(payload).execute()
        data = handle_response(res)
        return data[0] if data else {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/usuarios/{usuario_id}")
def update_usuario(usuario_id: int, u: UsuarioUpdate):
    try:
        payload = {k: v for k, v in u.dict().items() if v is not None}
        if not payload:
            raise HTTPException(status_code=400, detail="No hay campos para actualizar")
        res = cred.supabase.table("usuarios").update(payload).eq("id", usuario_id).execute()
        data = handle_response(res)
        return data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Actualizar una única columna dinámica (lo pediste antes)
@app.patch("/usuarios/{usuario_id}/campo")
def patch_campo(usuario_id: int, p: PatchField):
    try:
        payload = {p.column: p.value}
        res = cred.supabase.table("usuarios").update(payload).eq("id", usuario_id).execute()
        data = handle_response(res)
        if not data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado o no actualizado")
        return data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/usuarios/{usuario_id}")
def delete_usuario(usuario_id: int):
    try:
        # devuelve el registro eliminado
        res = cred.supabase.table("usuarios").delete().eq("id", usuario_id).execute()
        data = handle_response(res)
        if not data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"deleted": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

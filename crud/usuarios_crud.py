from fastapi import HTTPException
from typing import Any
from ..models.usuarios_models import UsuariosCreate, UsuariosUpdate, PatchField
from ..Cred import supabase_client

# ------------------- Helpers -------------------

def handle_response(res):
    if getattr(res, "error", None):
        raise HTTPException(status_code=500, detail=str(res.error))
    return res.data

def make_response(success: bool, message: str = "", data: Any = None):
    return {"success": success, "message": message, "data": data}

# ------------------- CRUD -------------------

def get_all():
    res = supabase_client.table("usuarios").select("*").execute()
    data = handle_response(res)
    return make_response(True, "Usuarios obtenidos", data)

def get_by_id(usuarios_id: int):
    res = supabase_client.table("usuarios").select("*").eq("id", usuarios_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Usuarios encontrado", data[0])
    return make_response(False, "Usuarios no encontrado")

def create(u: UsuariosCreate):
    payload = u.dict()
    if payload.get("fechanacimiento"):
        payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")
    res = supabase_client.table("usuarios").insert(payload).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Usuarios creado correctamente", data[0])
    return make_response(False, "No se pudo crear el usuarios")

def update(usuarios_id: int, u: UsuariosUpdate):
    payload = {k: v for k, v in u.dict().items() if v is not None}
    if payload.get("fechanacimiento"):
        payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")
    if not payload:
        return make_response(False, "No hay campos para actualizar")
    res = supabase_client.table("usuarios").update(payload).eq("id", usuarios_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Usuarios actualizado correctamente", data[0])
    return make_response(False, "Usuarios no encontrado o no actualizado")

def patch_field(usuarios_id: int, p: PatchField):
    payload = {p.column: p.value}
    res = supabase_client.table("usuarios").update(payload).eq("id", usuarios_id).execute()
    data = handle_response(res)
    if not data:
        raise HTTPException(status_code=404, detail="Usuarios no encontrado o no actualizado")
    return make_response(True, "Campo actualizado correctamente", data[0])

def delete(usuarios_id: int):
    res = supabase_client.table("usuarios").delete().eq("id", usuarios_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Usuarios eliminado correctamente", data[0])
    return make_response(False, "Usuarios no encontrado")

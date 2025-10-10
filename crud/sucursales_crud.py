from fastapi import HTTPException
from typing import Any
from ..models.sucursales_models import SucursalesCreate, SucursalesUpdate, PatchField
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
    res = supabase_client.table("sucursales").select("*").execute()
    data = handle_response(res)
    return make_response(True, "Sucursales obtenidos", data)

def get_by_id(sucursales_id: int):
    res = supabase_client.table("sucursales").select("*").eq("id", sucursales_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Sucursales encontrado", data[0])
    return make_response(False, "Sucursales no encontrado")

def create(u: SucursalesCreate):
    payload = u.dict()
    if payload.get("fechanacimiento"):
        payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")
    res = supabase_client.table("sucursales").insert(payload).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Sucursales creado correctamente", data[0])
    return make_response(False, "No se pudo crear el sucursales")

def update(sucursales_id: int, u: SucursalesUpdate):
    payload = {k: v for k, v in u.dict().items() if v is not None}
    if payload.get("fechanacimiento"):
        payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")
    if not payload:
        return make_response(False, "No hay campos para actualizar")
    res = supabase_client.table("sucursales").update(payload).eq("id", sucursales_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Sucursales actualizado correctamente", data[0])
    return make_response(False, "Sucursales no encontrado o no actualizado")

def patch_field(sucursales_id: int, p: PatchField):
    payload = {p.column: p.value}
    res = supabase_client.table("sucursales").update(payload).eq("id", sucursales_id).execute()
    data = handle_response(res)
    if not data:
        raise HTTPException(status_code=404, detail="Sucursales no encontrado o no actualizado")
    return make_response(True, "Campo actualizado correctamente", data[0])

def delete(sucursales_id: int):
    res = supabase_client.table("sucursales").delete().eq("id", sucursales_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Sucursales eliminado correctamente", data[0])
    return make_response(False, "Sucursales no encontrado")

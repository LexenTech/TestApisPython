from fastapi import HTTPException
from typing import Any
from ..models.roles_models import RolesCreate, RolesUpdate, PatchField
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
    res = supabase_client.table("roles").select("*").execute()
    data = handle_response(res)
    return make_response(True, "Roles obtenidos", data)

def get_by_id(roles_id: int):
    res = supabase_client.table("roles").select("*").eq("id", roles_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Roles encontrado", data[0])
    return make_response(False, "Roles no encontrado")

def create(u: RolesCreate):
    payload = u.dict()
    if payload.get("fechanacimiento"):
        payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")
    res = supabase_client.table("roles").insert(payload).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Roles creado correctamente", data[0])
    return make_response(False, "No se pudo crear el roles")

def update(roles_id: int, u: RolesUpdate):
    payload = {k: v for k, v in u.dict().items() if v is not None}
    if payload.get("fechanacimiento"):
        payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")
    if not payload:
        return make_response(False, "No hay campos para actualizar")
    res = supabase_client.table("roles").update(payload).eq("id", roles_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Roles actualizado correctamente", data[0])
    return make_response(False, "Roles no encontrado o no actualizado")

def patch_field(roles_id: int, p: PatchField):
    payload = {p.column: p.value}
    res = supabase_client.table("roles").update(payload).eq("id", roles_id).execute()
    data = handle_response(res)
    if not data:
        raise HTTPException(status_code=404, detail="Roles no encontrado o no actualizado")
    return make_response(True, "Campo actualizado correctamente", data[0])

def delete(roles_id: int):
    res = supabase_client.table("roles").delete().eq("id", roles_id).execute()
    data = handle_response(res)
    if data:
        return make_response(True, "Roles eliminado correctamente", data[0])
    return make_response(False, "Roles no encontrado")

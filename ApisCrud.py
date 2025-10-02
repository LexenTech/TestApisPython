# -------------------------------
# IMPORTACIONES
# -------------------------------
from datetime import date
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Any, Dict
import Credentials as cr  # tu cliente Supabase, asegúrate de que se llame correctamente

# -------------------------------
# CREACIÓN DE LA APP
# -------------------------------
app = FastAPI(title="API Usuarios - Salón")

# Habilitar CORS para que cualquier frontend pueda consumir la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # ✅ corregido
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# MODELOS DE DATOS
# -------------------------------
class UsuarioCreate(BaseModel):
    """Modelo para crear un usuario"""
    nombre: str
    apellidopaterno: str
    apellidomaterno: Optional[str] = None
    correo: str
    passwordhash: str
    telefono: Optional[str] = None
    rolid: int
    sucursalid: Optional[int] = None
    habilitado: Optional[bool] = True  # Nuevo campo, por defecto True
    fechanacimiento: date


class UsuarioUpdate(BaseModel):
    """Modelo para actualizar un usuario (todos los campos opcionales)"""
    nombre: Optional[str]
    apellidopaterno: Optional[str]
    apellidomaterno: Optional[str]
    correo: Optional[str]
    passwordhash: Optional[str]
    telefono: Optional[str]
    rolid: Optional[int]
    sucursalid: Optional[int]
    habilitado: Optional[bool]
    fechanacimiento: Optional[date]

class PatchField(BaseModel):
    """Modelo para actualizar un solo campo dinámico"""
    column: str
    value: Any

# -------------------------------
# HELPERS
# -------------------------------
def handle_response(res):
    """
    Maneja la respuesta de Supabase.
    Si hay error, lanza HTTPException 500.
    Si no, devuelve los datos.
    """
    if getattr(res, "error", None):
        raise HTTPException(status_code=500, detail=str(res.error))
    return res.data

def make_response(success: bool, message: str = "", data: Any = None):
    """
    Devuelve una respuesta uniforme para todos los endpoints.
    success: True si operación exitosa, False si hubo error
    message: mensaje descriptivo
    data: datos resultantes de la operación
    """
    return {
        "success": success,
        "message": message,
        "data": data
    }

# -------------------------------
# ENDPOINTS CRUD
# -------------------------------

# Obtener todos los usuarios
@app.get("/usuarios")
def get_usuarios():
    try:
        # Selecciona todos los usuarios y los ordena por id de manera ascendente
        res = cr.supabase.table("usuarios").select("*").execute()
        data = handle_response(res)
        return make_response(True, "Usuarios obtenidos", data)
    except Exception as e:
        return make_response(False, f"Error: {str(e)}")

# Obtener usuario por ID
@app.get("/usuarios/{usuario_id}")
def get_usuario(usuario_id: int):
    try:
        res = cr.supabase.table("usuarios").select("*").eq("id", usuario_id).execute()
        data = handle_response(res)
        if data:
            return make_response(True, "Usuario encontrado", data[0])
        else:
            return make_response(False, "Usuario no encontrado")
    except Exception as e:
        return make_response(False, f"Error: {str(e)}")

# Crear un nuevo usuario
@app.post("/usuarios/create", status_code=201)
def create_usuario(u: UsuarioCreate):
    try:
        payload = u.dict()
        # Convertir la fecha a string si existe
        if payload.get("fechanacimiento"):
            payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")

        res = cr.supabase.table("usuarios").insert(payload).execute()
        data = handle_response(res)
        if data:
            return make_response(True, "Usuario creado correctamente", data[0])
        else:
            return make_response(False, "No se pudo crear el usuario")
    except Exception as e:
        return make_response(False, f"Error: {str(e)}")




# Actualizar un usuario completo
@app.put("/usuarios/upd/{usuario_id}")
def update_usuario(usuario_id: int, u: UsuarioUpdate):
    try:
        # Solo enviar los campos que no son None
        payload = {k: v for k, v in u.dict().items() if v is not None}
        # Convertir la fecha a string si existe
        if payload.get("fechanacimiento"):
            payload["fechanacimiento"] = payload["fechanacimiento"].strftime("%Y-%m-%d")

        if not payload:
            return make_response(False, "No hay campos para actualizar")
        res = cr.supabase.table("usuarios").update(payload).eq("id", usuario_id).execute()
        data = handle_response(res)
        if data:
            return make_response(True, "Usuario actualizado correctamente", data[0])
        else:
            return make_response(False, "Usuario no encontrado o no actualizado")
    except Exception as e:
        return make_response(False, f"Error: {str(e)}")

# Actualizar un solo campo dinámico
@app.patch("/usuarios/{usuario_id}/campo")
def patch_campo(usuario_id: int, p: PatchField):
    try:
        payload = {p.column: p.value}
        res = cr.supabase.table("usuarios").update(payload).eq("id", usuario_id).execute()
        data = handle_response(res)
        if not data:
            raise HTTPException(status_code=404, detail="Usuario no encontrado o no actualizado")
        return make_response(True, "Campo actualizado correctamente", data[0])
    except Exception as e:
        return make_response(False, f"Error: {str(e)}")

# Eliminar un usuario
@app.delete("/usuarios/del/{usuario_id}")
def delete_usuario(usuario_id: int):
    try:
        res = cr.supabase.table("usuarios").delete().eq("id", usuario_id).execute()
        data = handle_response(res)
        if data:
            return make_response(True, "Usuario eliminado correctamente", data[0])
        else:
            return make_response(False, "Usuario no encontrado")
    except Exception as e:
        return make_response(False, f"Error: {str(e)}")


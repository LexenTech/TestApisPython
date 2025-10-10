from datetime import date
from pydantic import BaseModel
from typing import Optional, Any

class UsuariosBase(BaseModel):
    nombre: str
    apellidopaterno: str
    apellidomaterno: str
    correo: str
    telefono: str
    passwordhash: str
    rolid: int
    sucursalid: int
    habilitado: bool
    fechanacimiento: date

class UsuariosCreate(UsuariosBase):
    pass

class UsuariosUpdate(BaseModel):
    nombre: Optional[str] = None
    apellidopaterno: Optional[str] = None
    apellidomaterno: Optional[str] = None
    correo: Optional[str] = None
    telefono: Optional[str] = None
    passwordhash: Optional[str] = None
    rolid: Optional[int] = None
    sucursalid: Optional[int] = None
    habilitado: Optional[bool] = None
    fechanacimiento: Optional[date] = None

class PatchField(BaseModel):
    column: str
    value: Any
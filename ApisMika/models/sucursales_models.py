from datetime import date
from pydantic import BaseModel
from typing import Optional, Any

class SucursalesBase(BaseModel):
    nombresucursal: str
    calle: str
    numeroexterior: str
    numerointerior: str
    colonia: str
    codigopostal: str
    municipio: str
    estado: str
    pais: str
    telefono: str
    encargada: str

class SucursalesCreate(SucursalesBase):
    pass

class SucursalesUpdate(BaseModel):
    nombresucursal: Optional[str] = None
    calle: Optional[str] = None
    numeroexterior: Optional[str] = None
    numerointerior: Optional[str] = None
    colonia: Optional[str] = None
    codigopostal: Optional[str] = None
    municipio: Optional[str] = None
    estado: Optional[str] = None
    pais: Optional[str] = None
    telefono: Optional[str] = None
    encargada: Optional[str] = None

class PatchField(BaseModel):
    column: str
    value: Any
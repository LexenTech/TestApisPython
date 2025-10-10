from datetime import date
from pydantic import BaseModel
from typing import Optional, Any

class RolesBase(BaseModel):
    nombrerol: str

class RolesCreate(RolesBase):
    pass

class RolesUpdate(BaseModel):
    nombrerol: Optional[str] = None

class PatchField(BaseModel):
    column: str
    value: Any
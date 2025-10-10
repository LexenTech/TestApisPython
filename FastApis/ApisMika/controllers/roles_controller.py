from fastapi import APIRouter
from ApisMika.models.roles_models import RolesCreate, RolesUpdate, PatchField
from ApisMika.crud.roles_crud import get_all, get_by_id, create, update, patch_field, delete

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/")
def api_get_all():
    return get_all()

@router.get("/{item_id}")
def api_get_by_id(item_id: int):
    return get_by_id(item_id)

@router.post("/create", status_code=201)
def api_create(item: RolesCreate):
    return create(item)

@router.put("/upd/{item_id}")
def api_update(item_id: int, item: RolesUpdate):
    return update(item_id, item)

@router.patch("/{item_id}/campo")
def api_patch(item_id: int, p: PatchField):
    return patch_field(item_id, p)

@router.delete("/del/{item_id}")
def api_delete(item_id: int):
    return delete(item_id)

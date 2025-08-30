from fastapi import APIRouter, HTTPException, Form, Query
from typing import Optional
from core.models.store import Store
from core.models.medicine import Medicine
from core.schemas.schema import Store_Pydantic, Store_InPydantic, Medicine_Pydantic

router = APIRouter(prefix="/store", tags=["Store"])

@router.get("/")
async def do_nothing():
    return {"msg": "Works"}

@router.post("/signup")
async def create_store(
    storeName: str = Form(...),
    address: str = Form(...),
    storeOwnerName: str = Form(...)
):
    data = await Store.filter(
        store_name=storeName,
        location=address,
        store_owner_name=storeOwnerName
    ).first()
    if data:
        raise HTTPException(status_code=409, detail="Store already exists")

    new_store = await Store.create(
        store_name=storeName,
        location=address,
        store_owner_name=storeOwnerName
    )
    return await Store_Pydantic.from_tortoise_orm(new_store)

@router.post("/verify")
async def verify_store_owner(
    storeName: str = Form(...),
    storeOwnerName: Optional[str] = Form(None),
    address: Optional[str] = Form(None),
):
    q = Store.filter(store_name=storeName)
    if storeOwnerName:
        q = q.filter(store_owner_name=storeOwnerName)
    if address:
        q = q.filter(location=address)

    store = await q.first()
    if not store:
        raise HTTPException(status_code=404, detail="Store not found / owner not matched")
    return await Store_Pydantic.from_tortoise_orm(store)

@router.get("/medicine", response_model=list[Medicine_Pydantic])
async def fetch_medicine_of_store(store_id: int = Query(...)):
    return await Medicine_Pydantic.from_queryset(Medicine.filter(store_id=store_id).all())

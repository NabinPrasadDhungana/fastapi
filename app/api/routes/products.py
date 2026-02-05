from fastapi import APIRouter
from app.schemas.product import ProductCreate

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/")
def create_product(product: ProductCreate):
    return product
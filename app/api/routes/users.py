from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    return user

@router.get("/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

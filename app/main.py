from fastapi import FastAPI
from app.schemas.user import UserCreate, UserResponse
from app.api.routes import users, products

app = FastAPI(title="Learning FastAPI")

app.include_router(users.router)
app.include_router(products.router)


# @app.get("/")
# def root():
#     return {"message": "Hello FastAPI"}

# @app.get("/health")
# def health():
#     return {"status": "ok"}

# @app.post("/users")
# def create_user(user: UserCreate):
#     return {
#         "message": "User Created",
#         "user": user
#     }

# @app.post("/users", response_model=UserResponse)
# def create_user(user: UserCreate):
#     return user


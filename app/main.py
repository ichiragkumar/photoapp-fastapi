from fastapi import FastAPI
from app.api.routes import auth , users , photos
from app.db.session import engine
from app.db.base import Base



Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gallery App")


app.include_router(auth.router,  prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(photos.router, prefix="/photos", tags=["photos"])



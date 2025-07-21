from app.db.session import SessionLocal
from app.models.user import User
from app.core.security import get_password_hash

def init_db():
    db = SessionLocal()
    if not db.query(User).filter(User.email == "admin@example.com").first():
        user = User(email="admin@example.com", hashed_password=get_password_hash("admin"))
        db.add(user)
        db.commit()
        db.refresh(user)

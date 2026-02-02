from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.database import get_db
from app.schemas.users import UserCreate, UserResponse
from app.models.users import User

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        or_(
            User.user_email == user.user_email,
            User.user_phone == user.user_phone
        )
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="Email or phone already exists"
        )

    new_user = User(
        user_name=user.user_name,
        user_phone=user.user_phone,
        user_email=user.user_email,
        user_password=user.user_password,  # hashing later
        user_gender=user.user_gender.value,
        user_location=user.user_location
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.get("/", response_model=list[UserResponse])
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.put("/users/{user_id}", response_model=UserResponse)
def update_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    for key, value in db.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user      
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from counter import schemas, crud
from counter.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.User])
def all_users(db: Session = Depends(deps.get_db),
              skip: int = 0,
              limit: int = 100) -> List[schemas.User]:
    """
    Retrieve all user names from database.
    """
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users


@router.post("/", response_model=schemas.User)
def create_user(request: schemas.UserCreate, db: Session = Depends(deps.get_db)) -> schemas.User:
    """
    Create new user.
    """
    user = crud.user.get_by_username(db, username=request.username)
    if user:
        raise HTTPException(400, "User with that username already exists!")

    user = crud.user.create(db, user=request)

    return user

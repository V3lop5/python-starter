from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session

from counter.crud.base import CRUDBase

from counter.model import User
from counter.schemas import UserCreate, UserUpdate


# noinspection PyMethodMayBeStatic
class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def get_by_username(self, db: Session, *, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()

    def create(self, db: Session, *, user: UserCreate) -> User:
        db_obj = User(
            username=user.username,
            # TODO hash password
            hashed_password=user.password
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def authenticate(self, db: Session, *, username: str, password: str):
        user = self.get_by_username(db, username=username)
        if not user:
            return None
        if not password == password:
            return None
        return user


user = CRUDUser(User)

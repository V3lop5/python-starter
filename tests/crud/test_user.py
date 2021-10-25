from sqlalchemy.orm import Session

from counter import crud
from counter.schemas import UserCreate


def test_create_user(db: Session) -> None:
    username = "Harry"
    user_in = UserCreate(username=username, password="Potter")
    user = crud.user.create(db, user=user_in)
    assert user.username == username
    assert hasattr(user, "hashed_password")

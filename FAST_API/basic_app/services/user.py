from ..model.user import User
from sqlalchemy.orm import Session
from ..dto import user


def create_user(data: user.User, db: Session):
    user = User(name=data.name)
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user


def get_users(id: int, db):
    return db.query(User).filter(User.id == id).first()


def update(data: user.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    user.name = data.name
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def remove(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    db.delete(user)
    db.commit()
    return user
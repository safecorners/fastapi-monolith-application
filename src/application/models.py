from sqlalchemy import Boolean, Column, Integer, String

from application.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return (
            f"<User(id={self.id}, "
            f'email="{self.email}", '
            f'hashed_password="{self.hashed_password}", '
            f"is_active={self.is_active})>"
        )

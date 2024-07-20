from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from db.engine import Base


class User(Base):
    __tablename__ = "user"
    id = Column(String(256), primary_key=True, index=True, nullable=False)
    email = Column(String(256), unique=True, index=True, nullable=False)
    name = Column(String(256), index=True)
    username = Column(String(256), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)

    items = relationship("Task", back_populates="user")


class Task(Base):
    __tablename__ = "task"

    id = Column(String(256), primary_key=True, index=True, nullable=False)
    text = Column(String(256), index=True, nullable=False)
    user_id = Column(String, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="items")

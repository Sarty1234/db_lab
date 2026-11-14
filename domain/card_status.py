

from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class CardStatus(Base):
    __tablename__ = "card_status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))

    cards: Mapped[List["Card"]] = relationship(back_populates="card_status")

    def __repr__(self) -> str:
        return f"CardStatus(id={self.id!r}, name={self.name!r})"

    


from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class CardType(Base):
    __tablename__ = "card_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))

    cards: Mapped[List["Card"]] = relationship(back_populates="card_type")

    def __repr__(self) -> str:
        return f"CardType(id={self.id!r}, name={self.name!r})"

    


from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship, foreign
from .general_domain import Base

class CardPattern(Base):
    __tablename__ = "card_pattern"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    pattern_path: Mapped[Optional[str]] = mapped_column(String(255))

    cards: Mapped[List["Card"]] = relationship(
        "Card",
        back_populates="card_pattern",
        primaryjoin="foreign(Card.card_pattern_id) == CardPattern.id",
      )

    def __repr__(self) -> str:
        return f"CardPattern(id={self.id!r}, name={self.name!r})"

    
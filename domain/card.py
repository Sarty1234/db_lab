


from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class Card(Base):
    __tablename__ = "card"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[Optional[int]] = mapped_column(ForeignKey("account.id"))
    card_type_id: Mapped[Optional[int]] = mapped_column(ForeignKey("card_type.id"))
    card_status_id: Mapped[Optional[int]] = mapped_column(ForeignKey("card_status.id"))
    card_pattern_id: Mapped[Optional[int]] = mapped_column(Integer, nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(45))
    creation_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    number: Mapped[Optional[str]] = mapped_column(String(20))
    cvv: Mapped[Optional[str]] = mapped_column(String(5))
    pin: Mapped[Optional[str]] = mapped_column(String(5))
    secret_word: Mapped[Optional[str]] = mapped_column(String(100))

    account: Mapped[Optional["Account"]] = relationship(back_populates="cards")
    card_type: Mapped[Optional["CardType"]] = relationship(back_populates="cards")
    card_status: Mapped[Optional["CardStatus"]] = relationship(back_populates="cards")
    card_pattern: Mapped[Optional["CardPattern"]] = relationship(
      "CardPattern",
      back_populates="cards",
      primaryjoin="Card.card_pattern_id == CardPattern.id",
      foreign_keys=[card_pattern_id],
    )

    def __repr__(self) -> str:
        return f"Card(id={self.id!r}, number={self.number!r})"


    
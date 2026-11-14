

from datetime import datetime
from typing import Optional, List
from sqlalchemy import Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class Transaction(Base):
    __tablename__ = "transaction"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_id: Mapped[Optional[int]] = mapped_column(ForeignKey("account.id"))
    reciever_account_id: Mapped[Optional[int]] = mapped_column(ForeignKey("account.id"))
    datetime: Mapped[Optional[datetime]] = mapped_column(DateTime)
    amount: Mapped[Optional[int]] = mapped_column(Integer)
    description: Mapped[Optional[str]] = mapped_column(String(500))

    account: Mapped[Optional["Account"]] = relationship(
        foreign_keys=[account_id], 
        back_populates="transactions_sent"
    )
    receiver_account: Mapped[Optional["Account"]] = relationship(
        foreign_keys=[reciever_account_id], 
        back_populates="transactions_received"
    )

    def __repr__(self) -> str:
        return f"Transaction(id={self.id!r}, amount={self.amount!r}, datetime={self.datetime!r})"

    


from typing import List, Optional
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class Account(Base):
    __tablename__ = "account"

    id: Mapped[int] = mapped_column(primary_key=True)
    account_type_id: Mapped[Optional[int]] = mapped_column(ForeignKey("account_type.id"))
    account_status_id: Mapped[Optional[int]] = mapped_column(ForeignKey("account_status.id"))
    number: Mapped[Optional[str]] = mapped_column(String(45))
    credentials: Mapped[Optional[str]] = mapped_column(String(45))
    name: Mapped[Optional[str]] = mapped_column(String(45))
    balance: Mapped[Optional[int]] = mapped_column(Integer)
    creditscore: Mapped[Optional[int]] = mapped_column(Integer)


    account_type: Mapped[Optional["AccountType"]] = relationship(back_populates="accounts")
    account_status: Mapped[Optional["AccountStatus"]] = relationship(back_populates="accounts")
    client_associations: Mapped[List["ClientAccount"]] = relationship(back_populates="account")
    cards: Mapped[List["Card"]] = relationship(back_populates="account")

    
    transactions_sent: Mapped[List["Transaction"]] = relationship(
        foreign_keys="[Transaction.account_id]", 
        back_populates="account"
    )
    
    transactions_received: Mapped[List["Transaction"]] = relationship(
        foreign_keys="[Transaction.reciever_account_id]", 
        back_populates="receiver_account"
    )

    def __repr__(self) -> str:
        return f"Account(id={self.id!r}, number={self.number!r}, balance={self.balance!r})"

    
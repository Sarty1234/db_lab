

from typing import Optional, List
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class ClientAccount(Base):
    __tablename__ = "client_account"

    account_id: Mapped[int] = mapped_column(ForeignKey("account.id"), primary_key=True)
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), primary_key=True)
    account_access_status_id: Mapped[Optional[int]] = mapped_column(ForeignKey("account_access_status.id"))

    account: Mapped["Account"] = relationship(back_populates="client_associations")
    client: Mapped["Client"] = relationship(back_populates="account_associations")
    access_status: Mapped[Optional["AccountAccessStatus"]] = relationship(back_populates="client_accounts")

    def __repr__(self) -> str:
        return f"ClientAccount(account_id={self.account_id!r}, client_id={self.client_id!r})"

    


from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class AccountAccessStatus(Base):
    __tablename__ = "account_access_status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))

    client_accounts: Mapped[List["ClientAccount"]] = relationship(back_populates="access_status")

    def __repr__(self) -> str:
        return f"AccountAccessStatus(id={self.id!r}, name={self.name!r})"

    
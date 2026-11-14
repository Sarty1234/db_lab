

from typing import List, Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class AccountStatus(Base):
    __tablename__ = "account_status"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))

    accounts: Mapped[List["Account"]] = relationship(back_populates="account_status")

    def __repr__(self) -> str:
        return f"AccountStatus(id={self.id!r}, name={self.name!r})"

    
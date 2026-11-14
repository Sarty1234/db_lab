


from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(45))
    surname: Mapped[Optional[str]] = mapped_column(String(45))
    middlename: Mapped[Optional[str]] = mapped_column(String(45))
    phone: Mapped[Optional[str]] = mapped_column(String(15))
    email: Mapped[Optional[str]] = mapped_column(String(45))
    rnokpp: Mapped[Optional[str]] = mapped_column(String(45))
    fop: Mapped[Optional[str]] = mapped_column(String(45))
    photolink: Mapped[Optional[str]] = mapped_column(String(200))
    date_registered: Mapped[Optional[datetime]] = mapped_column(DateTime)


    secret_data: Mapped[Optional["ClientSecretData"]] = relationship(back_populates="client", uselist=False)
    account_associations: Mapped[List['ClientAccount']] = relationship(back_populates="client")

    def __repr__(self) -> str:
        return f"Client(id={self.id!r}, name={self.name!r}, surname={self.surname!r})"


    



from typing import Optional, List
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .general_domain import Base

class ClientSecretData(Base):
    __tablename__ = "client_secret_data"

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id"), primary_key=True)
    residence: Mapped[Optional[str]] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(500))
    is_on_fraud_watch: Mapped[Optional[bool]] = mapped_column(Boolean)
    war_veteran: Mapped[Optional[bool]] = mapped_column(Boolean)

    
    client: Mapped["Client"] = relationship(back_populates="secret_data")

    def __repr__(self) -> str:
        return f"ClientSecretData(client_id={self.client_id!r}, description={self.client!r})"

    
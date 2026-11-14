

from typing import Optional
from sqlalchemy.orm import Session
from domain.client import Client
from .base_dao import BaseDAO

class ClientDAO(BaseDAO[Client]):
    def __init__(self):
        super().__init__(Client)

    def get_by_email(self, session: Session, email: str) -> Optional[Client]:
        return session.query(Client).filter(Client.email == email).first()

    
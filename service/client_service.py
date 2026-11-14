


from typing import List, Optional
from sqlalchemy.orm import Session
from dao.client_dao import ClientDAO
from domain.client import Client

class ClientService:
    def __init__(self):
        self.dao = ClientDAO()

    def get_by_id(self, session: Session, client_id: int) -> Optional[Client]:
        return self.dao.get_by_id(session, client_id)

    def get_all(self, session: Session, skip: int = 0, limit: int = 100) -> List[Client]:
        return self.dao.get_all(session, skip, limit)

    def create(self, session: Session, data: dict) -> Client:
        return self.dao.create(session, data)

    def update(self, session: Session, client_id: int, data: dict) -> Optional[Client]:
        client = self.dao.get_by_id(session, client_id)
        if client:
            return self.dao.update(session, client, data)
        return None

    def delete(self, session: Session, client_id: int) -> bool:
        return self.dao.delete(session, client_id)


    
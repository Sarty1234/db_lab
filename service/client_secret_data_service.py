

from typing import List, Optional
from sqlalchemy.orm import Session
from dao.client_secret_data_dao import ClientSecretDataDAO
from domain.client_secret_data import ClientSecretData

class ClientSecretDataService:
    def __init__(self):
        self.dao = ClientSecretDataDAO()

    def get_by_id(self, session: Session, client_id: int) -> Optional[ClientSecretData]:
        return self.dao.get_by_id(session, client_id)

    def create(self, session: Session, data: dict) -> ClientSecretData:
        return self.dao.create(session, data)

    def update(self, session: Session, client_id: int, data: dict) -> Optional[ClientSecretData]:
        secret_data = self.dao.get_by_id(session, client_id)
        if secret_data:
            return self.dao.update(session, secret_data, data)
        return None

    def delete(self, session: Session, client_id: int) -> bool:
        return self.dao.delete(session, client_id)

    
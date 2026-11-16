


from typing import List, Optional
from sqlalchemy.orm import Session
from dao.client_account_dao import ClientAccountDAO
from domain.client_account import ClientAccount

class ClientAccountService:
    def __init__(self):
        self.dao = ClientAccountDAO()

    def get_by_id(self, session: Session, account_id: int) -> Optional[ClientAccount]:
        return self.dao.get_by_id(session, account_id)

    def get_all(self, session: Session, skip: int = 0, limit: int = 100) -> List[ClientAccount]:
        return self.dao.get_all(session, skip, limit)

    def create(self, session: Session, data: dict) -> ClientAccount:
        return self.dao.create(session, data)

    def create_by_names(self, session: Session, data: dict):
        return self.dao.create_by_names(
            session,
            client_name=data.get("client_name"),
            client_surname=data.get("client_surname"),
            account_name=data.get("account_name"),
            account_access_status_id=data.get("account_access_status_id"),
        )

    def create_with_procedure(self, session: Session, data: dict) -> ClientAccount:
        new_id = self.dao.call_insert_procedure(session, data)
        return self.dao.get_by_id(session, new_id)

    def update(self, session: Session, account_id: int, data: dict) -> Optional[ClientAccount]:
        account = self.dao.get_by_id(session, account_id)
        if account:
            return self.dao.update(session, account, data)
        return None

    def delete(self, session: Session, account_id: int) -> bool:
        return self.dao.delete(session, account_id)

    
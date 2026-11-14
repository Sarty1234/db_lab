

from typing import List, Optional
from sqlalchemy.orm import Session
from domain.client_account import ClientAccount
from .base_dao import BaseDAO

class ClientAccountDAO(BaseDAO[ClientAccount]):
    def __init__(self):
        super().__init__(ClientAccount)

    def get_by_id(self, session: Session, account_id: int, client_id: int) -> Optional[ClientAccount]:
        return session.get(ClientAccount, (account_id, client_id))

    def delete(self, session: Session, account_id: int, client_id: int) -> bool:
        db_obj = self.get_by_id(session, account_id, client_id)
        if db_obj:
            session.delete(db_obj)
            session.commit()
            return True
        return False

    def get_by_client(self, session: Session, client_id: int) -> List[ClientAccount]:
        return session.query(ClientAccount).filter(ClientAccount.client_id == client_id).all()

    def get_by_account(self, session: Session, account_id: int) -> List[ClientAccount]:
        return session.query(ClientAccount).filter(ClientAccount.account_id == account_id).all()

    



from typing import List, Optional
from sqlalchemy.orm import Session
from dao.account_dao import AccountDAO
from domain.account import Account

class AccountService:
    def __init__(self):
        self.dao = AccountDAO()

    def get_by_id(self, session: Session, account_id: int) -> Optional[Account]:
        return self.dao.get_by_id(session, account_id)

    def get_all(self, session: Session, skip: int = 0, limit: int = 100) -> List[Account]:
        return self.dao.get_all(session, skip, limit)

    def create(self, session: Session, data: dict) -> Account:
        return self.dao.create(session, data)

    def create_with_procedure(self, session: Session, data: dict) -> Account:
        new_id = self.dao.call_insert_procedure(session, data)
        return self.dao.get_by_id(session, new_id)

    def update(self, session: Session, account_id: int, data: dict) -> Optional[Account]:
        account = self.dao.get_by_id(session, account_id)
        if account:
            return self.dao.update(session, account, data)
        return None

    def delete(self, session: Session, account_id: int) -> bool:
        return self.dao.delete(session, account_id)

    
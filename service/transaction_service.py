


from typing import List, Optional
from sqlalchemy.orm import Session
from dao.transaction_dao import TransactionDAO
from domain.transaction import Transaction

class TransactionService:
    def __init__(self):
        self.dao = TransactionDAO()

    def get_by_id(self, session: Session, transaction_id: int) -> Optional[Transaction]:
        return self.dao.get_by_id(session, transaction_id)

    def get_all(self, session: Session, skip: int = 0, limit: int = 100) -> List[Transaction]:
        return self.dao.get_all(session, skip, limit)

    def create(self, session: Session, data: dict) -> Transaction:
        return self.dao.create(session, data)

    def update(self, session: Session, transaction_id: int, data: dict) -> Optional[Transaction]:
        transaction = self.dao.get_by_id(session, transaction_id)
        if transaction:
            return self.dao.update(session, transaction, data)
        return None

    def delete(self, session: Session, transaction_id: int) -> bool:
        return self.dao.delete(session, transaction_id)


    
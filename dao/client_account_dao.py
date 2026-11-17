

from typing import List, Optional
from sqlalchemy.orm import Session
from domain.client_account import ClientAccount
from .base_dao import BaseDAO
from fastapi import HTTPException
from sqlalchemy import text

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

    def create_by_names(
      self,
      session: Session,
      client_name: str,
      client_surname: str,
      account_name: str,
      account_access_status_id: int,
    ):
        stmt = text("""
                INSERT INTO client_account (account_id, client_id, account_access_status_id)
                SELECT 
                    (SELECT id FROM account WHERE name = :account_name LIMIT 1),
                    (SELECT id FROM client WHERE name = :client_name AND surname = :client_surname LIMIT 1),
                    :access_status_id
                FROM DUAL
                WHERE 
                    (SELECT id FROM account WHERE name = :account_name LIMIT 1) IS NOT NULL
                    AND 
                    (SELECT id FROM client WHERE name = :client_name AND surname = :client_surname LIMIT 1) IS NOT NULL
            """)

        result = session.execute(
            stmt,
            {
                "account_name": account_name,
                "client_name": client_name,
                "client_surname": client_surname,
                "access_status_id": account_access_status_id,
            },
        )
        session.commit()

        if result.rowcount == 0:
            raise HTTPException(
                status_code=404,
                detail=(
                    "Client or account not found"
                ),
            )
        return True

    
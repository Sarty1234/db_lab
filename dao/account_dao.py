

from domain.account import Account
from .base_dao import BaseDAO
from sqlalchemy import text
from sqlalchemy.orm import Session

class AccountDAO(BaseDAO[Account]):
    def __init__(self):
        super().__init__(Account)


    def call_insert_procedure(self, session: Session, data: dict) -> int:
        sql = text("""
            CALL sp_insert_account(
                :account_type_id, 
                :account_status_id, 
                :number, 
                :credentials, 
                :name, 
                :balance, 
                :creditscore, 
                @new_id
            )
        """)
        
        session.execute(sql, data)
        
        result = session.execute(text("SELECT @new_id")).scalar()
        session.commit()
        
        return result

    
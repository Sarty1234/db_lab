


from typing import List, Optional
from sqlalchemy.orm import Session
from dao.card_dao import CardDAO
from domain.card import Card
from sqlalchemy import text

class CardService:
    def __init__(self):
        self.dao = CardDAO()

    def get_by_id(self, session: Session, card_id: int) -> Optional[Card]:
        return self.dao.get_by_id(session, card_id)

    def get_all(self, session: Session, skip: int = 0, limit: int = 100) -> List[Card]:
        return self.dao.get_all(session, skip, limit)

    def create(self, session: Session, data: dict) -> Card:
        return self.dao.create(session, data)

    def update(self, session: Session, card_id: int, data: dict) -> Optional[Card]:
        card = self.dao.get_by_id(session, card_id)
        if card:
            return self.dao.update(session, card, data)
        return None

    def delete(self, session: Session, card_id: int) -> bool:
        return self.dao.delete(session, card_id)

    def insert_10_patterns(self, db: Session):
        sql = text("CALL mydb.sp_insert_10_card_patterns()")
        db.execute(sql)
        db.commit()


    
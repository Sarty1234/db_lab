

from domain.card_status import CardStatus
from .base_dao import BaseDAO

class CardStatusDAO(BaseDAO[CardStatus]):
    def __init__(self):
        super().__init__(CardStatus)

        
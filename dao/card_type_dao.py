

from domain.card_type import CardType
from .base_dao import BaseDAO

class CardTypeDAO(BaseDAO[CardType]):
    def __init__(self):
        super().__init__(CardType)

        
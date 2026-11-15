


from domain.card_pattern import CardPattern
from .base_dao import BaseDAO

class CardPatternDAO(BaseDAO[CardPattern]):
    def __init__(self):
        super().__init__(CardPattern)

        
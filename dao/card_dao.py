


from domain.card import Card
from .base_dao import BaseDAO

class CardDAO(BaseDAO[Card]):
    def __init__(self):
        super().__init__(Card)

        
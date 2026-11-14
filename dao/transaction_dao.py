

from domain.transaction import Transaction
from .base_dao import BaseDAO

class TransactionDAO(BaseDAO[Transaction]):
    def __init__(self):
        super().__init__(Transaction)

        
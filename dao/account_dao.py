

from domain.account import Account
from .base_dao import BaseDAO

class AccountDAO(BaseDAO[Account]):
    def __init__(self):
        super().__init__(Account)

    
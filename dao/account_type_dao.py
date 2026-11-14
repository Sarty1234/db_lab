

from domain.account_type import AccountType
from .base_dao import BaseDAO

class AccountTypeDAO(BaseDAO[AccountType]):
    def __init__(self):
        super().__init__(AccountType)

        
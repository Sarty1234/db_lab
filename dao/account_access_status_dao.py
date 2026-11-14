
from domain.account_access_status import AccountAccessStatus
from .base_dao import BaseDAO

class AccountAccessStatusDAO(BaseDAO[AccountAccessStatus]):
    def __init__(self):
        super().__init__(AccountAccessStatus)

        



from domain.account_status import AccountStatus
from .base_dao import BaseDAO

class AccountStatusDAO(BaseDAO[AccountStatus]):
    def __init__(self):
        super().__init__(AccountStatus)

        
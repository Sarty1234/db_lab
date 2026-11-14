

from domain.client_secret_data import ClientSecretData
from .base_dao import BaseDAO

class ClientSecretDataDAO(BaseDAO[ClientSecretData]):
    def __init__(self):
        super().__init__(ClientSecretData)

    
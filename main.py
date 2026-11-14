# main.py updates
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from domain import Base, Client
from dao.client_dao import ClientDAO
from dao.account_dao import AccountDAO
from service.client_service import ClientService

load_dotenv()
DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(DATABASE_URL, echo=False)

def test_daos():
    # client_dao = ClientDAO()
    account_dao = AccountDAO()
    c = ClientService()

    with Session(engine) as session:
        # 1. Get client by ID using DAO
        client = c.get_all(session)
        print(f"Retrieved via DAO: {client!r}")

        # # 2. Use custom DAO method
        # if client and client.email:
        #     found_by_email = client_dao.get_by_email(session, client.email)
        #     print(f"Found by email query: {found_by_email!r}")

        # # 3. Get all accounts using the generic DAO
        # accounts = account_dao.get_all(session, limit=50)
        # print(f"Accounts found: {accounts}")

if __name__ == "__main__":
    test_daos()
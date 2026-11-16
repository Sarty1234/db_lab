

from fastapi import FastAPI, HTTPException, Depends
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


from service import (
    ClientService,
    ClientSecretDataService,
    AccountService,
    CardService,
    TransactionService,
    ClientAccountService,
)
from dto import (
    NewClientItem, UpdateClientItem,
    NewClientSecretItem, UpdateClientSecretItem,
    NewAccountItem, UpdateAccountItem,
    NewCardItem, UpdateCardItem,
    NewTransactionItem,
    NewClientAccountByName,
)

load_dotenv()
DATABASE_URL = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="Banking API", version="1.0")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize service instances
client_service = ClientService()
secret_service = ClientSecretDataService()
account_service = AccountService()
card_service = CardService()
transaction_service = TransactionService()
client_account_service = ClientAccountService()




####################### CLIENTS #######################
@app.get("/clients", tags=['Clients'], summary="Get all clients or filter by ID")
def read_clients(id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if id:
        client = client_service.get_by_id(db, id)
        if not client:
            raise HTTPException(status_code=404, detail="Client not found")
        return client
    return client_service.get_all(db, skip=skip, limit=limit)

@app.post("/clients", tags=['Clients'], summary="Create new client", status_code=201)
def create_client(new_client: NewClientItem, db: Session = Depends(get_db)):
    client_service.create(db, new_client.dict())
    return {"success": True, "message": "Client added successfully"}

@app.put("/clients", tags=['Clients'], summary="Update client")
def update_client(client_data: UpdateClientItem, db: Session = Depends(get_db)):
    result = client_service.update(db, client_data.id, client_data.dict(exclude_unset=True))
    if not result:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"success": True, "message": "Client updated successfully"}

@app.delete("/clients/{client_id}", tags=['Clients'], summary="Delete client")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    result = client_service.delete(db, client_id)
    if not result:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"success": True, "message": "Client removed successfully"}




####################### CLIENT ACCOUNT #######################
@app.get("/client-accounts", tags=["Client Account"], summary="Get all client-account links")
def read_client_accounts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return client_account_service.get_all(db, skip=skip, limit=limit)

@app.get("/client-accounts/by-client/{client_id}", tags=["Client Account"], summary="Get accounts by client ID")
def get_accounts_by_client(client_id: int, db: Session = Depends(get_db)):
    return client_account_service.dao.get_by_client(db, client_id)

@app.get("/client-accounts/by-account/{account_id}", tags=["Client Account"], summary="Get clients by account ID")
def get_clients_by_account(account_id: int, db: Session = Depends(get_db)):
    return client_account_service.dao.get_by_account(db, account_id)

@app.post("/client-accounts/by-names", tags=["Client Account"], summary="Link client and account by real names (M:M task)", status_code=201)
def create_client_account_by_names(data: NewClientAccountByName, db: Session = Depends(get_db)):
    client_account_service.create_by_names(db, data.model_dump())
    return { "success": True, "message": "Link created successfully", }


@app.delete("/client-accounts", tags=["Client Account"], summary="Delete client-account link by composite primary key")
def delete_client_account(account_id: int, client_id: int, db: Session = Depends(get_db)):
    result = client_account_service.delete(db, account_id, client_id)
    if not result:
        raise HTTPException(status_code=404, detail="Client-Account link not found")
    return {"success": True, "message": "Link successfully removed"}




####################### CLIENT SECRET DATA #######################
@app.get("/client-secrets/{client_id}", tags=['Client Secrets'], summary="Get client secret data by client ID")
def read_client_secret(client_id: int, db: Session = Depends(get_db)):
    secret = secret_service.get_by_id(db, client_id)
    if not secret:
        raise HTTPException(status_code=404, detail="Secret data not found for this client")
    return secret

@app.post("/client-secrets", tags=['Client Secrets'], summary="Create client secret data", status_code=201)
def create_client_secret(new_secret: NewClientSecretItem, db: Session = Depends(get_db)):
    secret_service.create(db, new_secret.dict())
    return {"success": True, "message": "Client secret data added successfully"}

@app.put("/client-secrets", tags=['Client Secrets'], summary="Update client secret data")
def update_client_secret(secret_data: UpdateClientSecretItem, db: Session = Depends(get_db)):
    result = secret_service.update(db, secret_data.client_id, secret_data.dict(exclude_unset=True))
    if not result:
        raise HTTPException(status_code=404, detail="Secret data not found")
    return {"success": True, "message": "Client secret data updated successfully"}

@app.delete("/client-secrets/{client_id}", tags=['Client Secrets'], summary="Delete client secret data")
def delete_client_secret(client_id: int, db: Session = Depends(get_db)):
    result = secret_service.delete(db, client_id)
    if not result:
        raise HTTPException(status_code=404, detail="Secret data not found")
    return {"success": True, "message": "Client secret data removed successfully"}




####################### ACCOUNTS #######################
@app.get("/accounts", tags=['Accounts'], summary="Get all accounts or filter by ID")
def read_accounts(id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if id:
        account = account_service.get_by_id(db, id)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found")
        return account
    return account_service.get_all(db, skip=skip, limit=limit)

# @app.post("/accounts", tags=['Accounts'], summary="Create new account", status_code=201)
# def create_account(new_account: NewAccountItem, db: Session = Depends(get_db)):
#     account_service.create(db, new_account.dict())
#     return {"success": True, "message": "Account added successfully"}

@app.post("/accounts", tags=['Accounts'], summary="Create new account with Stored Procedure", status_code=201)
def create_account_via_procedure(new_account: NewAccountItem, db: Session = Depends(get_db)):
    account_service.create_with_procedure(db, new_account.dict())
    return { "success": True, "message": "Account added successfully" }

@app.put("/accounts", tags=['Accounts'], summary="Update account")
def update_account(account_data: UpdateAccountItem, db: Session = Depends(get_db)):
    result = account_service.update(db, account_data.id, account_data.dict(exclude_unset=True))
    if not result:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"success": True, "message": "Account updated successfully"}

@app.delete("/accounts/{account_id}", tags=['Accounts'], summary="Delete account")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    result = account_service.delete(db, account_id)
    if not result:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"success": True, "message": "Account removed successfully"}




####################### CARDS #######################
@app.get("/cards", tags=['Cards'], summary="Get all cards or filter by ID")
def read_cards(id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if id:
        card = card_service.get_by_id(db, id)
        if not card:
            raise HTTPException(status_code=404, detail="Card not found")
        return card
    return card_service.get_all(db, skip=skip, limit=limit)

@app.post("/cards", tags=['Cards'], summary="Create new card", status_code=201)
def create_card(new_card: NewCardItem, db: Session = Depends(get_db)):
    card_service.create(db, new_card.dict())
    return {"success": True, "message": "Card added successfully"}

@app.put("/cards", tags=['Cards'], summary="Update card")
def update_card(card_data: UpdateCardItem, db: Session = Depends(get_db)):
    result = card_service.update(db, card_data.id, card_data.dict(exclude_unset=True))
    if not result:
        raise HTTPException(status_code=404, detail="Card not found")
    return {"success": True, "message": "Card updated successfully"}

@app.delete("/cards/{card_id}", tags=['Cards'], summary="Delete card")
def delete_card(card_id: int, db: Session = Depends(get_db)):
    result = card_service.delete(db, card_id)
    if not result:
        raise HTTPException(status_code=404, detail="Card not found")
    return {"success": True, "message": "Card removed successfully"}




####################### TRANSACTIONS #######################
@app.get("/transactions", tags=['Transactions'], summary="Get all transactions or filter by ID")
def read_transactions(id: int = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if id:
        tx = transaction_service.get_by_id(db, id)
        if not tx:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return tx
    return transaction_service.get_all(db, skip=skip, limit=limit)

@app.post("/transactions", tags=['Transactions'], summary="Create new transaction", status_code=201)
def create_transaction(new_tx: NewTransactionItem, db: Session = Depends(get_db)):
    transaction_service.create(db, new_tx.dict())
    return {"success": True, "message": "Transaction recorded successfully"}

@app.delete("/transactions/{transaction_id}", tags=['Transactions'], summary="Delete transaction")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    result = transaction_service.delete(db, transaction_id)
    if not result:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"success": True, "message": "Transaction removed successfully"}





if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)


    
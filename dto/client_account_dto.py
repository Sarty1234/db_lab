

from pydantic import BaseModel


class NewClientAccountByName(BaseModel):
  client_name: str
  client_surname: str
  account_name: str
  account_access_status_id: int

  


from pydantic import BaseModel
from typing import Optional

class NewClientSecretItem(BaseModel):
    client_id: int
    residence: Optional[str] = None
    description: Optional[str] = None
    is_on_fraud_watch: bool = False
    war_veteran: bool = False

class UpdateClientSecretItem(BaseModel):
    client_id: int
    residence: Optional[str] = None
    description: Optional[str] = None
    is_on_fraud_watch: Optional[bool] = None
    war_veteran: Optional[bool] = None


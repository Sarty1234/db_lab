

from pydantic import BaseModel, Field
from typing import Optional


class NewAccountItem(BaseModel):
    account_type_id: int
    account_status_id: int
    number: str = Field(..., max_length=45)
    credentials: str = Field(..., max_length=45)
    name: str = Field(..., max_length=45)
    balance: int = 0
    creditscore: int = 0
    

class UpdateAccountItem(BaseModel):
    id: int
    number: Optional[str] = Field(None, max_length=20)
    balance: Optional[float] = None
    creditscore: Optional[int] = None
    account_type_id: Optional[int] = None
    account_status_id: Optional[int] = None

    
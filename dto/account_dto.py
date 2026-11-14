

from pydantic import BaseModel, Field
from typing import Optional

class NewAccountItem(BaseModel):
    number: str = Field(..., max_length=20)
    balance: float = 0.0
    creditscore: Optional[int] = None
    account_type_id: Optional[int] = None
    account_status_id: Optional[int] = None

class UpdateAccountItem(BaseModel):
    id: int
    number: Optional[str] = Field(None, max_length=20)
    balance: Optional[float] = None
    creditscore: Optional[int] = None
    account_type_id: Optional[int] = None
    account_status_id: Optional[int] = None

    
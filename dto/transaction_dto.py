

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NewTransactionItem(BaseModel):
    amount: float = Field(..., gt=0, description="Transaction amount must be greater than zero")
    date: Optional[datetime] = None
    account_id: int
    receiver_account_id: int


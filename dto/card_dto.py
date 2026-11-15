


from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NewCardItem(BaseModel):
    number: str = Field(..., min_length=16, max_length=16)
    cvv: str = Field(..., min_length=3, max_length=4)
    pin: str = Field(..., min_length=4, max_length=4)
    creation_date: Optional[datetime] = None
    account_id: int
    card_type_id: Optional[int] = None
    card_status_id: Optional[int] = None
    card_pattern_id: Optional[int] = None

class UpdateCardItem(BaseModel):
    id: int
    card_status_id: Optional[int] = None


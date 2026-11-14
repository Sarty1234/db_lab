

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class NewClientItem(BaseModel):
    name: str = Field(..., max_length=45)
    surname: str = Field(..., max_length=45)
    middlename: Optional[str] = Field(None, max_length=45)
    phone: str = Field(..., max_length=15)
    email: str = Field(..., max_length=45)
    rnokpp: Optional[str] = Field(None, max_length=45)
    fop: Optional[str] = Field(None, max_length=45)
    photolink: Optional[str] = Field(None, max_length=200)
    date_registered: Optional[datetime] = None

class UpdateClientItem(BaseModel):
    id: int
    name: Optional[str] = Field(None, max_length=45)
    surname: Optional[str] = Field(None, max_length=45)
    middlename: Optional[str] = Field(None, max_length=45)
    phone: Optional[str] = Field(None, max_length=15)
    email: Optional[str] = Field(None, max_length=45)
    rnokpp: Optional[str] = Field(None, max_length=45)
    fop: Optional[str] = Field(None, max_length=45)
    photolink: Optional[str] = Field(None, max_length=200)


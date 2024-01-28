from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class DonationBase(BaseModel):
    comment: Optional[str]
    full_amount: Optional[int] = Field(None, gt=0)


class DonationCreate(DonationBase):
    full_amount: int = Field(..., gt=0)


class DonationDB(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationList(DonationDB):
    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    user_id: Optional[int]

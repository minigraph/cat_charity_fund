from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, validator


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str]
    full_amount: Optional[int] = Field(None, gt=0)

    class Config:
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1)
    full_amount: int = Field(..., gt=0)


class CharityProjectUpdate(CharityProjectBase):
    @validator('name')
    def name_cannot_be_null(cls, value):
        if value is None or not len(value):
            raise ValueError('Имя не может быть пустым!')
        return value

    @validator('description')
    def description_cannot_be_null(cls, value):
        if value is None or not len(value):
            raise ValueError('Описание не может быть пустым!')
        return value


class CharityProjectDB(CharityProjectBase):
    id: int
    create_date: datetime
    close_date: Optional[datetime]
    invested_amount: Optional[int]
    fully_invested: Optional[bool]

    class Config:
        orm_mode = True

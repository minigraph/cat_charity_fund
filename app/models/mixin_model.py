from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer
from sqlalchemy.orm import declarative_mixin


@declarative_mixin
class TimestampMixin:
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)


@declarative_mixin
class AmountMixin:
    full_amount = Column(Integer)
    invested_amount = Column(Integer, default=0)
    fully_invested = Column(Boolean, default=False)

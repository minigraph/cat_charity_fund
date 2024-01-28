from sqlalchemy import Column, String, Text

from app.core.db import Base

from .mixin_model import AmountMixin, TimestampMixin


class CharityProject(TimestampMixin, AmountMixin, Base):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)

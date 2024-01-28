from sqlalchemy import Column, ForeignKey, Integer, Text

from app.core.db import Base

from .mixin_model import AmountMixin, TimestampMixin


class Donation(TimestampMixin, AmountMixin, Base):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

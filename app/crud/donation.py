from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):

    async def get_by_user(
            self, session: AsyncSession, user: User
    ):
        donations = await session.execute(
            select(Donation).where(
                Donation.user_id == user.id
            )
        )
        return donations.scalars().all()

    async def get_active_donations(
            self, session: AsyncSession
    ):
        donations = await session.execute(
            select(Donation).where(
                Donation.full_amount != Donation.invested_amount
            ).order_by(Donation.create_date)
        )
        return donations.scalars().all()


donation_crud = CRUDDonation(Donation)

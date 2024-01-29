from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.donation import donation_crud
from app.models import User
from app.schemas.donation import DonationCreate, DonationDB, DonationList
from app.services.invest_donation import divided_donations

router = APIRouter()


@router.post(
    '/',
    response_model=DonationDB,
    response_model_exclude_none=True,
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    """создаем пожертвование текущего пользоватея."""

    new_donation = await donation_crud.create(
        donation, session, user
    )
    await divided_donations(session)
    return new_donation


@router.get(
    '/',
    response_model=list[DonationList],
)
async def get_all_donations(
        session: AsyncSession = Depends(get_async_session)
):
    """Получает список всех пожертвований."""

    return await donation_crud.get_multi(session)


@router.get(
    '/my',
    response_model=list[DonationDB],
)
async def get_my_donations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """Получает список всех пожертвований текущего пользователя."""

    return await donation_crud.get_by_user(
        session=session, user=user
    )

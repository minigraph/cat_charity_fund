from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charity_project_crud, donation_crud


async def close_object(obj, amount: int):
    obj.invested_amount = amount
    obj.close_date = datetime.now()
    obj.fully_invested = True
    return obj


async def divided_donations(session: AsyncSession):
    donations = await donation_crud.get_active_donations(session)
    if not donations:
        return

    projects = await charity_project_crud.get_active_projects(session)
    if not projects:
        return

    change_objects = []
    for donation in donations:
        free_sum = donation.full_amount - donation.invested_amount

        for project in projects:
            if project in change_objects:
                change_objects.remove(project)

            need_sum = project.full_amount - project.invested_amount
            if free_sum == need_sum:
                change_objects.append(
                    await close_object(donation, donation.full_amount)
                )
                change_objects.append(
                    await close_object(project, project.full_amount)
                )
                projects.remove(project)
                break
            elif free_sum > need_sum:
                free_sum -= need_sum
                change_objects.append(
                    await close_object(project, project.full_amount)
                )
                projects.remove(project)
            else:
                project.invested_amount += free_sum
                change_objects.append(project)
                change_objects.append(
                    await close_object(donation, donation.full_amount)
                )
                break

    for obj in change_objects:
        session.add(obj)
    await session.commit()
    for obj in change_objects:
        await session.refresh(obj)

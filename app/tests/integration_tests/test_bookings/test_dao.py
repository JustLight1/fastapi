from datetime import datetime

import pytest

from app.bookings.dao import BookingDAO
from app.database import async_session_maker


@pytest.mark.parametrize(
    'user_id, room_id',
    [
        (2, 2),
        (2, 3),
        (1, 4),
        (1, 4),
    ]
)
async def test_booking_crud(user_id, room_id):
    # Добавление брони
    async with async_session_maker() as session:
        new_booking = await BookingDAO.add(
            user_id=user_id,
            room_id=room_id,
            date_from=datetime.strptime('2023-07-10', '%Y-%m-%d'),
            date_to=datetime.strptime('2023-07-24', '%Y-%m-%d'),
            session=session
        )

        assert new_booking.user_id == user_id
        assert new_booking.room_id == room_id

        # Проверка добавления брони
        new_booking = await BookingDAO.find_one_or_none(
            session,
            id=new_booking.id
        )

        assert new_booking is not None

        # Удаление брони
        await BookingDAO.delete(
            session,
            id=new_booking.id,
            user_id=user_id,
        )

        # Проверка удаления брони
        deleted_booking = await BookingDAO.find_one_or_none(
            session,
            id=new_booking.id
        )
        assert deleted_booking is None

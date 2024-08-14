from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter, or_f
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from sqlalchemy.ext.asyncio import AsyncSession
from keyboards.kb import del_kb

from keyboards.kb import admin_kb


# from database.orm_query import (
#     orm_add_product,
#     orm_delete_product,
#     orm_get_product,
#     orm_get_products,
#     orm_update_product,
# )

from filters.chat_types import ChatTypeFilter, IsAdmin


admin_router = Router()
admin_router.message.filter(ChatTypeFilter(["private"]), IsAdmin())


@admin_router.message(Command('administrator'))
async def check_list(message: Message):
    await message.answer(
        'Приветствую Вас администратор!',
        reply_markup=admin_kb
    )


@admin_router.message(F.text.lower() == '📜Просмотреть текущие заказы!')
async def check_list(message: Message):
    await message.answer(
        'Все текущие заказы!',
        reply_markup=admin_kb
    )

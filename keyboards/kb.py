from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove
)

from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📝Сделать заказ!'),
            KeyboardButton(text='📖 О нас')
        ],
        [
            KeyboardButton(text='⚙️Техподдержка')
        ]

    ],
    resize_keyboard=True,
    input_field_placeholder='Сделайте выбор!'
)

del_kb = ReplyKeyboardRemove()


admin_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📜Просмотреть текущие заказы!'),
        ]

    ],
    resize_keyboard=True,
    input_field_placeholder='Сделайте выбор!'
)
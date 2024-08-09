from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

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
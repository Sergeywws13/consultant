from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
import keyboards.kb as kb


user_opened = Router()

@user_opened.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello, you get your ID?', reply_markup=kb.main_kb)


@user_opened.message(F.text.lower() == 'yes')
async def answer_yes(message: Message):
    await message.answer(
        f'Вот ваш ID {message.from_user.id}',
        reply_markup=ReplyKeyboardRemove()
    )

@user_opened.message(F.text.lower() == 'no')
async def answer_yes(message: Message):
    await message.answer(
        'Bye',
        reply_markup=ReplyKeyboardRemove()
    )
    
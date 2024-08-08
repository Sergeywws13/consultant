from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
import keyboards.kb as kb
from utils import text


user_opened = Router()

@user_opened.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello user!!!!!!!!', reply_markup=kb.main_kb)


@user_opened.message(F.text.lower() == '📝сделать заказ!')
async def answer_yes(message: Message):
    await message.answer(
        'Заполните анкету!',
        reply_markup=kb.main_kb
    )

@user_opened.message(F.text.lower() == '📖 о нас')
async def answer_yes(message: Message):
    await message.answer(
        text.text_about,
        reply_markup=kb.main_kb
    )


@user_opened.message(F.text.lower() == '⚙️техподдержка')
async def answer_yes(message: Message):
    await message.answer(
        'По всем вопросам обращаться @makootooo!',
        reply_markup=kb.main_kb
    )
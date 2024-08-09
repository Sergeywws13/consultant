from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart, or_f
import keyboards.kb as kb
from utils import text


user_opened = Router()

@user_opened.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello user!!!!!!!!', reply_markup=kb.main_kb)


@user_opened.message(or_f(Command('create'), F.text.lower() == '📝сделать заказ!'))
async def create_list(message: Message):
    await message.answer(
        text.text_create,
        reply_markup=kb.main_kb
    )


@user_opened.message(or_f(Command('about'), F.text.lower() == '📖 о нас'))
async def about_me(message: Message):
    await message.answer(
        text.text_about,
        reply_markup=kb.main_kb
    )


@user_opened.message(or_f(Command('settings'), F.text.lower() == '⚙️техподдержка'))
async def settings(message: Message):
    await message.answer(
        'По всем вопросам обращаться @makootooo!',
        reply_markup=kb.main_kb
    )


@user_opened.message(F.contact)
async def about_me(message: Message):
    await message.answer(
        f'Номер получен',
        reply_markup=kb.main_kb
    )
    await message.answer(str(message.contact))


@user_opened.message(F.text)
async def about_me(message: Message):
    await message.answer(
        'Введите команду из меню!',
        reply_markup=kb.main_kb
    )
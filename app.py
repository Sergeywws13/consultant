import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv # type: ignore
from common.bot_cmds_list import private

load_dotenv(find_dotenv())

from handlers import user_open


async def main():
    bot = Bot(token=os.getenv('TOKEN'))
    dp = Dispatcher()
    # Routers
    dp.include_router(user_open.user_opened)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

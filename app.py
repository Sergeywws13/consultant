import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from dotenv import find_dotenv, load_dotenv # type: ignore
from common.bot_cmds_list import private
from database.models import async_main

load_dotenv(find_dotenv())

from handlers import user_open
from handlers import user_group
from handlers import admin_private


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

# bot.my_admins_list = []


async def main():
    try:
        await async_main()
    except Exception as e:
        logging.error(f"Database error: {e}")


    dp.include_router(user_open.user_opened)
    dp.include_router(user_group.user_group_router)
    dp.include_router(admin_private.admin_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

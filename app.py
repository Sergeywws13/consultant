import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import user_open


BOT_TOKEN = "6942331878:AAEwewxE1_ZhQn0secJYnQHtE_-rKqYSTIs"



async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(user_open.user_opened)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

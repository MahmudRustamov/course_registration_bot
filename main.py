import asyncio
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from core.config import BOT_TOKEN
from handlers import register

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()



async def main():
    dp.include_router(router=register.router)
    await dp.start_polling(bot, polling_timeout=0)


if __name__ == "__main__":
    asyncio.run(main())
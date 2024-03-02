import asyncio
from aiogram import Bot, Dispatcher
import navalny


async def main():
    bot = Bot(token="**********************************************")
    dp = Dispatcher()
    dp.include_routers(navalny.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers.commands_start import router as start_router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)

    print("🤖 Bot is running...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Bot stopped.")

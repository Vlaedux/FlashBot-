from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("👋 Привіт! Я FlashBot. Готовий допомогти з навчанням!")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("📚 Команди:\n/start — почати роботу\n/help — допомога")

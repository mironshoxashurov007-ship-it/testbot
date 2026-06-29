import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = "8765778226:AAHP6PNXG6-rBu80LDwpz6kof1OMur9jkas"

bot = Bot(token=TOKEN)
dp = Dispatcher()


def menu():
    kb = ReplyKeyboardBuilder()
    kb.button(text="👋 Salom")
    kb.button(text="🕒 Vaqt")
    kb.button(text="ℹ️ Men haqimda")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        f"Assalomu alaykum, {message.from_user.first_name}! 👋\n"
        "Botga xush kelibsiz.",
        reply_markup=menu()
    )


@dp.message(F.text == "👋 Salom")
async def hello(message: Message):
    await message.answer("Salom! 😊 Qalaysiz?")


@dp.message(F.text == "🕒 Vaqt")
async def time(message: Message):
    from datetime import datetime
    now = datetime.now().strftime("%H:%M:%S")
    await message.answer(f"⏰ Hozirgi vaqt: {now}")


@dp.message(F.text == "ℹ️ Men haqimda")
async def about(message: Message):
    await message.answer(
        f"👤 Ism: {message.from_user.full_name}\n"
        f"🆔 ID: {message.from_user.id}\n"
        f"📛 Username: @{message.from_user.username}"
    )


@dp.message()
async def echo(message: Message):
    await message.answer(f"Siz yozdingiz:\n\n{message.text}")


async def main():
    print("✅ Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
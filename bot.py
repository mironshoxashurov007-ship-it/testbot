import os
import asyncio
import yt_dlp

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart

TOKEN = "8778339346:AAEGRyVEHT_6dPXZrAvljgayhtomUkOMF14"

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🎬 Video URL yuboring.\n"
        "Men uni eng yuqori sifatda yuklab beraman."
    )


@dp.message(F.text)
async def download_video(message: Message):
    url = message.text.strip()

    msg = await message.answer("📥 Video yuklanmoqda...")

    try:
        ydl_opts = {
            "format": "bv*+ba/best",
            "merge_output_format": "mp4",
            "outtmpl": "%(title)s.%(ext)s",
            "noplaylist": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        if not filename.endswith(".mp4"):
            filename = os.path.splitext(filename)[0] + ".mp4"

        await msg.edit_text("📤 Video yuborilmoqda...")

        await message.answer_document(
            FSInputFile(filename),
            caption="✅ Eng yuqori mavjud sifatda yuklandi."
        )

        os.remove(filename)

    except Exception as e:
        await msg.edit_text(f"❌ Xatolik:\n{e}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
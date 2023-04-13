from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from googletrans import Translator
from langdetect import detect

translator = Translator()
dest = "en"

TOKEN = "your token"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def button1(message: types.Message):
    await bot.send_message(message.from_user.id, "Hello, I'm translator-bot!")


@dp.message_handler()
async def translate(message: types.Message):
    srcl = detect(message.text)
    translated_text = translator.translate(
        message.text, src=srcl, dest=dest).text
    await bot.send_message(message.from_user.id, translated_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

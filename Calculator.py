from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import TOKEN
import webbrowser

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'calculator'])
async def start(message: types.Message):
    await message.reply("Send me an expression to evaluate, like 2+2 or 6/3")


@dp.message_handler()
async def process(message: types.Message):
    try:
        result = eval(message.text)
        await message.reply(f"The result of {message.text} is {result}")
    except Exception:
        await message.reply("Sorry, I couldn't evaluate that expression!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

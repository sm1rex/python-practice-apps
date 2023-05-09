from aiogram import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = ""

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Open Youtube'))
keyboard.add(KeyboardButton('Send image'))


@dp.message_handler(commands=['start'])
async def send_keyboard(message: types.Message):
    await message.answer('Choose operation: ', reply_markup=keyboard)


@dp.message_handler(text='Open Youtube')
async def open_youtube(message: types.Message):
    await message.answer('Open yt: https://www.youtube.com/')


@dp.message_handler(text='Send image')
async def send_picture(message: types.Message):
    await bot.send_photo(message.from_user.id, 'https://images.unsplash.com/photo-1483232539664-d89822fb5d3e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cGhvdG8lMjBiYWNrZ3JvdW5kfGVufDB8fDB8fA%3D%3D&w=1000&q=80')

if __name__ == "__main__":
    executor.start_polling(dp)

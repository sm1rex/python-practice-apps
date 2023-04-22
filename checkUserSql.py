import sqlite3
from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute(
    ''' CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)  ''')
conn.commit()

bot = Bot(token='YOUR TOKEN')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    cursor = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    if user is not None:
        await bot.send_message(message.chat.id, "You registered yet.")
    else:
        cursor.execute(
            "INSERT INTO users (id, name) VALUES (?, ?)", (user_id, user_name))
        conn.commit()
        await bot.send_message(message.chat.id, "WELCOME TO MY BOT)")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

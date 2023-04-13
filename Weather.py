from aiogram import *
from config import *
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import requests
import bs4
from bs4 import BeautifulSoup as BS

r = requests.get('https://sinoptik.ua/погода-киев')
html = BS(r.content, 'html.parser')

Token = "your token"

bot = Bot(token=Token)
dp = Dispatcher(bot)

#  если id - #
for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    desc = el.select('.wDescription .rSide .description')[0].text


@dp.message_handler(commands=['start'])
async def button1(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, погода на сегодня:\n" + t_min + ', ' + t_max + ', ' + '\n' + '\n' + desc)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

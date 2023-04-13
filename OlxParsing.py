import requests
from bs4 import *
from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import *
url = "https://www.olx.ua/d/uk/nedvizhimost/kvartiry/prodazha-kvartir/"

html = requests.get(url=url).text

TOKEN = "5480970372:AAGltOT7oWNZq8dp9BrUe8LaS_TBBe9asX4"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
doc = BeautifulSoup(html, "html.parser")


@dp.message_handler(commands=['start'])
async def button1(message: types.Message):
    await bot.send_message(message.from_user.id, "Дякую, що скористалися нашим ботом!")
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton(text="Київ", callback_data="butt_kyiv")
    button2 = InlineKeyboardButton(text="Харків:", callback_data="butt_khar")
    markup.add(button1, button2)
    await bot.send_message(message.chat.id, "Оберіть місто у якому Ви хочете знайти квартиру:", reply_markup=markup)


# @dp.callback_query_handler(lambda c: c.data == "butt_kyiv")
# async def func(call: types.callback_query):
#     await bot.send_message(call.message.from_user.id, "Ви обрали місто Київ, оберіть цінову категорію!")


@dp.callback_query_handler(lambda c: c.data == "butt_kyiv")
async def func(call: types.callback_query):
    url2 = "https://www.olx.ua/d/uk/nedvizhimost/kvartiry/prodazha-kvartir/kiylov/?currency=UAH"
    html2 = requests.get(url=url2).text
    doc2 = BeautifulSoup(html2, "html.parser")
    allLinks2 = doc2.findAll('div', {'class': 'css-1sw7q4x'})
    for i in allLinks2:
        await bot.send_message(call.message.chat.id, ("https://www.olx.ua" +
                                                      i.find('a', {'class': 'css-rc5s2u'}).get('href').strip()))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

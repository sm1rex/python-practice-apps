import requests
from bs4 import BeautifulSoup
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ParseMode
from aiogram.utils import executor

TOKEN = "YOUR TOKEN"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# создаем список квартир, который мы отобразим в инлайн меню
flats = []

# Функция для получения данных


async def parse_data(city):
    global flats
    url = f'https://www.olx.ua/d/uk/nedvizhimost/kvartiry/prodazha-kvartir/{city}/?currency=UAH'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all('div', {'class': 'offer-wrapper'})
    flats = []
    for card in cards:
        title = card.find('strong').text.strip()
        price = card.find('p', {'class': 'price'}).text.strip()
        link = card.find('a')['href']
        location = card.find('i', {'class': 'location'}).text.strip()
        flat_info = f'Title: {title}\n Price: {price}\nLocation: {location}\nLink: {link}'
        flats.append(flat_info)


# Функция для создания инлайн меню с городами

async def create_city_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    cities = ['kiev', 'kharkov', 'odessa']
    for city in cities:
        button = InlineKeyboardButton(
            text=f"{city.capitalize()}", callback_data=f"city_{city}")
        keyboard.add(button)
    return keyboard


#  функция для создания меню с квартирами

async def create_flat_menu():
    keyboard = InlineKeyboardMarkup(row_width=1)
    for idx, flat in enumerate(flats):
        button = InlineKeyboardButton(
            text=f"Flat #{idx+1}", callback_data=f"flat_{idx}")
        keyboard.add(button)
    return keyboard


# /start
@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = await create_city_menu()
    await message.answer("Welcome! Please, select a city:", reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('city_'))
async def process_city_callback(callback_query: types.CallbackQuery, state: FSMContext):
    city = callback_query.data.split('_')[1]
    await parse_data(city)
    keyboard = await create_flat_menu()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, reply_markup=keyboard, text="")


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('flat_'))
async def process_flat_callback(callback_query: types.CallbackQuery, state: FSMContext):
    flat_idx = int(callback_query.data.split('_')[1])
    flat = flats[flat_idx]
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(chat_id=callback_query.from_user.id, text=flat, parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

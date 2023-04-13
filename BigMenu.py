from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import *
TOKEN = "YOUR TOKEN"

bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


class MenuStates(StatesGroup):
    menu = State()
    firstm = State()
    second = State()
    last = State()


@dp.message_handler(commands=["start"])
async def any_msg(message: types.Message):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(
        text="1button", callback_data="first")
    second_button = types.InlineKeyboardButton(
        text="2button", callback_data="second")
    keyboardmain.add(first_button, second_button)
    await message.answer("testing kb", reply_markup=keyboardmain)
    await MenuStates.menu.set()


@dp.callback_query_handler(lambda c: c.data == "first", state=MenuStates.menu)
async def process_btn1(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    rele1 = InlineKeyboardButton(text="1t", callback_data="1")
    rele2 = InlineKeyboardButton(text="2t", callback_data="2")
    rele3 = InlineKeyboardButton(text="3t", callback_data="3")
    backbtn = InlineKeyboardButton(text="Back", callback_data="menu")
    keyboard.add(rele1, rele2, rele3, backbtn)
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="replaced text", reply_markup=keyboard)
    await MenuStates.firstm.set()


@dp.callback_query_handler(lambda c: c.data == "second", state=MenuStates.menu)
async def process_btn2(callback_query: types.CallbackQuery, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup()
    rele1 = InlineKeyboardButton(text="another", callback_data="gg")
    backbtn = InlineKeyboardButton(text="Back", callback_data="menu")
    keyboard.add(rele1, backbtn)
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="replaced text", reply_markup=keyboard)
    await MenuStates.second.set()


@dp.callback_query_handler(lambda c: c.data == "menu", state=[MenuStates.firstm, MenuStates.second])
async def process_btn3(callback_query: types.CallbackQuery, state: FSMContext):
    keyboardmain = types.InlineKeyboardMarkup(row_width=2)
    first_button = types.InlineKeyboardButton(
        text="1button", callback_data="first")
    second_button = types.InlineKeyboardButton(
        text="2button", callback_data="second")
    keyboardmain.add(first_button, second_button)
    await bot.edit_message_text(chat_id=callback_query.message.chat.id, message_id=callback_query.message.message_id, text="menu", reply_markup=keyboardmain)
    await MenuStates.menu.set()


@dp.callback_query_handler(lambda c: c.data in ['1', '2', '3'], state=[MenuStates.firstm])
async def proccess123(callback_query: types.CallbackQuery, state: FSMContext):
    await bot.answer_callback_query()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

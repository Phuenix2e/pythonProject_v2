
'''import sounddevice as sd
import numpy as np

def print_sound(indata, outdata, frames, time, status):
    counter = 0
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > 56:
        counter +=1
        print(counter)

with sd.Stream(callback=print_sound):
    sd.sleep(10000000)'''

'''
class BANAN():
    def __int__(self):
        self.full_name = None
        self.rating = 10
        self.banned = False

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Для начала, пожалуйста, предоставьте нам информацию о себе.")
    await message.answer("Вышли фото")

@dp.message(Command("unban"))
async def ban(message: types.Message,user_dict: dict[str], command: CommandObject):
        if message.from_user.first_name == "Constantin":
            if command.args in user_dict:
                user_dict[command.args].banned =False
                await message.answer(f"User{command.args} user was unbanned")

@dp.message(F.new_chat_members)
async def new_user(message: types.message,user_dict: dict[str]):
    for user in message.new_chat_members:
        if not user.id in user_dict:
                QUser = user()
                QUser.full_name = user.full_name
                user_dict[user.id] = QUser
                await  message.reply(f"Здравствуйте, {user.full_name}. прочти пж :{user.can_read_all_gtow}")
                await  message.reply(f"Rules of the grup:https://telegra.ph/bot-11-07-12")
        elif user_dict[user.id].banned:
            await  message.bot.ban_chat_member(message.caht.id)

@dp(F.text)
async  def анализ_матов(mesage:types.message, user_dict: dict[str]):
    if "fack" in message.text.lower() or "Блять" in mesage.text.lower():
        print(str(mesage.from_user.id))
        if user_dict[str(mesage.from_user.id)].rating>=5:
            await  message.reply(f"Всё с головой в порядке ?, {message.from_user.username}!")
            user_dict[message.from_user.id].banned = True
        else:
            await message.reply(f"Прости {message.from_user.username}, но маты в сделку не входили.")
            await  message.bot.ban_chat_member(message.chat.id, message.from_user.id)
            user_dict[message.from_user.id].banned = True

async def main():
    await dp.start_polling(bot , user_dict = {})'''
'''
import asyncio
import  logging
from aiogram import Bot,Dispatcher,types
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram import html,F
from config import Config
from pydantic_settings import  BaseSettings,SettingsConfigDict
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.markdown import hide_link
from pydantic import SecretStr
import os

logging.basicConfig(level=logging.INFO)
bot = Bot(token=Config.bot_token.get_secret_value(),parse_mode="HTML")
dp = Dispatcher()
'''
import asyncio
import  logging
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot,Dispatcher,types
from aiogram.filters.command import Command
from aiogram.filters import CommandObject
from aiogram import html,F
from config_reader import config
from pydantic_settings import  BaseSettings,SettingsConfigDict
from aiogram.types import FSInputFile, URLInputFile, BufferedInputFile
from aiogram.utils.markdown import hide_link
from pydantic import SecretStr
import os



logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
keyboard.add(KeyboardButton("Количество пострадавших"))
keyboard.add(KeyboardButton("Травмы"))
keyboard.add(KeyboardButton("Информатор"))
keyboard.add(KeyboardButton("Геолокация"))

user_responses = {}

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добро пожаловать! Этот бот предназначен для сбора информации о чрезвычайных ситуациях. "
                         "Пожалуйста, используйте кнопки для ответов.", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Количество пострадавших")
async def ask_num_of_casualties(message: types.Message):
    await message.answer("Сколько человек пострадало?")
    user_responses[message.chat.id] = {"Количество пострадавших": None}

@dp.message_handler(lambda message: message.text == "Травмы")
async def ask_injuries(message: types.Message):
    await message.answer("Какие травмы получены?")
    user_responses[message.chat.id] = {"Травмы": None}

@dp.message_handler(lambda message: message.text == "Информатор")
async def ask_informant(message: types.Message):

    await message.answer("Кто сообщает о несчастном случае?")
    user_responses[message.chat.id] = {"Информатор": None}

@dp.message_handler(lambda message: message.text == "Геолокация")
async def ask_location(message: types.Message):
    await message.answer("Пожалуйста, отправьте геолокацию.")
    user_responses[message.chat.id] = {"Геолокация": None}

@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def process_location(message: types.Message):
    user_responses[message.chat.id]["Геолокация"] = message.location
    await message.answer("Спасибо за предоставленную информацию!")

async def main():
    await  dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

    dp.start_polling(dp, skip_updates=True)






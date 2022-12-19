from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base import sqlite_db
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('общение с ботом через ЛС, напишите ему:n\ t.me/Roma_Pizza_bot')

#@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9-00 до 23-00, Пт-Сб с 10-00 до 23-00')

#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'г. Пятигорск, ул. Калинина,2', reply_markup=kb_client)

inkb = InlineKeyboardMarkup(row_width=2)
inkb_1 = InlineKeyboardButton(text='Пицца на тонком тесте', url='https://roma-pizza.ru')
inkb_2 = InlineKeyboardButton(text='Пицца на пышном тесте', url='https://roma-pizza.ru')
inkb.add(inkb_1, inkb_2)
@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await message.answer('Разделы меню', reply_markup=inkb)
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])

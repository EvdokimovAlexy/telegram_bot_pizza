from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот вышел в ОНЛАЙН')


# *********************************КЛИЕНТСКАЯ ЧАСТЬ*******************************
@dp.message_handler(commands=['start', 'help'])

async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита')
        await message.delete()
    except:
        await message.reply('общение с ботом через ЛС, напишите ему:n\ t.me/Roma_Pizza_bot')

@dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9-00 до 23-00, Пт-Сб с 10-00 до 23-00')

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'г. Пятигорск, ул. Калинина,2')



# *********************************АДМИНСКАЯ ЧАСТЬ*******************************


# *********************************ОБЩАЯ ЧАСТЬ*******************************

@dp.message_handler()
async def echo_sent(message: types.Message):
    if message.text == "Привет":
        await message.answer('Приветствую тебя о великий пиццеман!')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

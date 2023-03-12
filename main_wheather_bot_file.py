import requests
import datetime
from config import open_weather_token, tg_bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот успешно запустился!')

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply('Привет! Напиши мне название города и я пришлю тебе прогноз погоды!'
                        '\nДля дополнительной информации вызови команду /help')

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await message.reply('Бот сообщает данные о погоде в городе!'
                        '\nНазвание города должно быть написано на английском или русском языках.')

@dp.message_handler()
async def get_weather(message: types.Message):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        #pprint(data)

        city = data["name"]
        cup_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        feels_like = data["main"]["feels_like"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f"Погода в городе: {city}\nТемпература: {cup_weather} °С\n"
              f"Влажность: {humidity}%\n"
              f"Давление: {pressure} мм.рт.ст\n"
              f"Ощущается как: {feels_like} °С\n"
              f"Скорость ветра: {wind} м/с\n "
              f"Время рассвета: {sunrise_timestamp}\n "
              f"Время заката: {sunset_timestamp}\n"
              f"Продолжительность светого дня: {lenght_of_the_day}\n"
              "Не хорошего дня, а замечательного!"

              )
    except:
        await message.reply('Проверьте название города')




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
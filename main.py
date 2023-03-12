import requests
import datetime
from pprint import pprint
from config import open_weather_token

def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
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

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
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



    except Exception as ex:
        print(ex)
        print('Проверьте название города')


def main():
    city = input('Введите город:')
    get_weather(city, open_weather_token)

if __name__ == '__main__':
    main()

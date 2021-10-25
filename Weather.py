import random
import os
from os import path
import pyttsx3
import speech_recognition as speech_recog
import pyaudio as recog
r = speech_recog.Recognizer()
mic = speech_recog.Microphone()

# Python программа для поиска текущей
# детали погоды любого города
# используя openweathermap api
  
# импорт необходимых модулей
while True:
  import requests, json
  import pyttsx3

  engine = pyttsx3.init()     # инициализация движка

# зададим свойства
  engine.setProperty('rate', 150)     # скорость речи
  engine.setProperty('volume', 0.9)   # громкость (0-1)

  engine.say("погода")      # запись фразы в очередь  # запись фразы в очередь

# очистка очереди и воспроизведение текста
  engine.runAndWait()

# выполнение кода останавливается, пока весь текст не сказан



  
  # Введите свой ключ API здесь

  api_key = "0dc78a26f442bfc4f6578a4b729f41c9"

  
  # base_url переменная для хранения URL

  base_url = "http://api.openweathermap.org/data/2.5/weather?"

  
  # Дать название города
  engine.say("Скажи имя города по английски, в котором хочешь посмотреть погоду")
  engine.runAndWait()
  with mic as audio_file:
    r.adjust_for_ambient_noise(audio_file)
    audio = r.listen(audio_file)
    print("I think please wait")
    try:
      city_name = r.recognize(audio)
    except LookupError:
      continue


      
  
  
  # complete_url переменная для хранения
  # полный адрес URL

  complete_url = base_url + "appid=" + api_key + "&q=" + city_name

  
  # получить метод модуля запросов
  # вернуть объект ответа

  response = requests.get(complete_url)

  
  # json метод объекта ответа
  # преобразовать данные формата json в
  # данные формата питона

  x = response.json()

  
  # Теперь x содержит список вложенных словарей
  # Проверьте, что значение ключа "cod" равно
  # "404", значит город найден иначе,
  # город не найден

  if x["cod"] != "404":

  

    # сохранить значение "main"

    # введите переменную y

      y = x["main"]

  

    # сохранить значение, соответствующее

    # к "временному" ключу y

      current_temperature = y["temp"] - 273.15
      a = int(current_temperature)
      current_temperature = float(a)

  

    # сохранить значение, соответствующее

    # к клавише "давления" у

      current_pressure = y["pressure"] * 0.750064
      п = int(current_pressure)
      current_pressure = float(п)
  

    # сохранить значение, соответствующее

    # к клавише «влажность» у

      current_humidiy = y["humidity"]

  

    # сохранить значение «погода»

    # введите переменную z

      z = x["weather"]

  

    # сохранить значение, соответствующее

    # к ключу "описание" в

    # 0 индекс z

      weather_description = z[0]["description"]

  

    # вывести следующие значения
      engine.say("Температура(в градусах по Цельсию) = " +

                      str(current_temperature) + 

            "\n Атмосферное давление (в милиметрах ртутного столба) = " +

                      str(current_pressure) +

            "\n влажность(в %) = " +

                      str(current_humidiy) +

            "\n описание = " +

                      str(weather_description))
      engine.runAndWait()
      print("Температура(в градусах по Цельсию) = " +

                      str(current_temperature) + 

            "\n Атмосферное давление (в мм рт. ст.) = " +

                      str(current_pressure) +

            "\n влажность(в %) = " +

                      str(current_humidiy) +

            "\n описание = " +

                      str(weather_description))

  

  else:

      print(" City Not Found ")

# -*- coding: utf-8 -*-

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get10days(urlincome):
    url = 'https://ua.sinoptik.ua/погода-' + str(urlincome) + "/10-днів"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    days = []
    date = []
    temperature = []
    link = []
    for counter in range(1, 11):
        bd = "bd" + str(counter)
        day = soup.find(id=bd)
        link.append(
            "http:" + str(day.find(class_='day-link').attrs['data-link']))
        days.append(day.find(class_='day-link').text)
        date.append(day.find(class_='date').text +
                    ' ' + day.find(class_='month').text)
        temperature.append(day.find(class_='temperature').text)

    wheather = pd.DataFrame(
        {
            'Day': days,
            'Date': date,
            'Temperature': temperature,
            'Link': link
        })
    print (wheather)
    namefile = "wheather-" + str(urlincome) + ".csv"
    wheather.to_csv(namefile)


print("ПРОГРАМА ПРОГНОЗА ПОГОДИ З САЙТУ SINOPTIK.UA НА 10 ДНІВ")

get10days(input("Наберіть назву міста (українською) > "))

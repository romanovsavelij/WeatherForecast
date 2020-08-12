import string
import requests
from http import HTTPStatus


class InvalidFormDataError(ValueError):
    pass


class WeatherForecast:
    def __init__(self, country, city: string):
        if city is None:
            city = ''
        if country is None:
            country = ''

        self.country = country
        self.city = city

        self.temp = 0
        self.humidity = 0
        self.wind_speed = 0

    def update_forecast(self) -> None:
        key = '31c578367136fce7972f2c3942fe0f3f'
        api = 'http://api.openweathermap.org/data/2.5/weather'
        key = '31c578367136fce7972f2c3942fe0f3f'

        location = self.city + ',' + self.country

        payload = {'q': location, 'units': 'metric', 'appid': key}
        r = requests.get(api, params=payload)
        if r.status_code != HTTPStatus.OK:
            raise InvalidFormDataError(f'Can\'t find forecast for {self.country}, {self.city}')

        data = r.json()
        self.temp = data['main']['temp']
        self.humidity = data['main']['humidity']
        self.wind_speed = data['wind']['speed']

from django.shortcuts import render

from utils.analyzer import ForecastAnalyzer
from utils.forecast import WeatherForecast, InvalidFormDataError
from http import HTTPStatus


def forecast(request):
    country = request.GET.get('country')
    city = request.GET.get('city')
    if not city:
        city = 'Capital'

    weather = WeatherForecast(country, city)
    try:
        weather.update_forecast()
    except InvalidFormDataError:
        return render(request, 'forecast-not-fount.html', status=HTTPStatus.UNPROCESSABLE_ENTITY)

    analyzer = ForecastAnalyzer(weather)
    comment = analyzer.get_comment()

    args = {'temperature': weather.temp, 'humidity': weather.humidity,
            'wind_speed': weather.wind_speed, 'comment': comment, 'city': city}

    return render(request, 'forecast.html', args)

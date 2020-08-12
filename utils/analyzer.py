import string
from utils.forecast import WeatherForecast
from utils.constants import HEATING_COMMENT, WARM_COMMENT, COLD_COMMENT, RAIN_COMMENT


class ForecastAnalyzer:
    def __init__(self, forecast: WeatherForecast):
        self.forecast = forecast

    def get_clothes_recommendation(self) -> string:
        if self.forecast.temp > 30:
            return HEATING_COMMENT
        elif self.forecast.temp > 15:
            return WARM_COMMENT
        else:
            return COLD_COMMENT

    def get_humidity_comment(self) -> string:
        if self.forecast.humidity > 50:
            return RAIN_COMMENT
        return ''

    def get_comment(self) -> string:
        clothes_recommendation = self.get_clothes_recommendation()
        humidity_comment = self.get_humidity_comment()
        return clothes_recommendation + ' ' + humidity_comment
import requests
from secrets import TEQUILA_ENDPOINT, TEQUILA_API_KEY
import datetime as dt


class FlightSearch:
    def __init__(self):
        self.endpoint = TEQUILA_ENDPOINT
        self.api_key = TEQUILA_API_KEY
        self.cities = list()

    def get_city_code(self, city):
        headers = {
            "apikey": self.api_key,
        }
        parameters = {
            "term": city,
            # "location_types": "city",
        }
        response = requests.get(
            url=self.endpoint,
            params=parameters,
            headers=headers,
        )
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def get_code_list(self, list_of_cities):
        city_codes = list()
        for city in list_of_cities:
            city_codes.append(self.get_city_code(city[0]))
        return city_codes


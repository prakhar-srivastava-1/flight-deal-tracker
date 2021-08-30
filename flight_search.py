import requests
from secrets import TEQUILA_ENDPOINT, TEQUILA_API_KEY, TEQUILA_ENDPOINT_FLIGHT
import datetime as dt


class FlightSearch:
    def __init__(self):
        self.endpoint = TEQUILA_ENDPOINT
        self.flight_search_endpoint = TEQUILA_ENDPOINT_FLIGHT
        self.api_key = TEQUILA_API_KEY
        self.cities = list()

    @staticmethod
    def format_date(raw_date):
        return f"{raw_date.strftime('%d')}/{raw_date.strftime('%m')}/{raw_date.strftime('%Y')}"

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

    def search_flights(self, destination, price_to, source="LON"):
        now = dt.datetime.now()
        future = now + dt.timedelta(days=6 * 30)

        from_date = self.format_date(now)
        to_date = self.format_date(future)

        parameters = {
            "fly_from": source,
            "fly_to": destination,
            "date_from": from_date,
            "date_to": to_date,
            "curr": "GBP",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "one_for_city": 1,
            "price_to": int(price_to),
            "asc": 1,
        }
        headers = {
            "apikey": self.api_key,
        }
        response = requests.get(
            url=self.flight_search_endpoint,
            headers=headers,
            params=parameters
        )

        response.raise_for_status()
        return response.json()["data"]
        # return response.json()["data"][0]
        # print(from_date, to_date)

    @staticmethod
    def get_cheapest_flight(list_of_flights):
        cheapest_flight = list_of_flights[0]
        for flight in list_of_flights[1:]:
            if int(cheapest_flight.price) > int(flight.price):
                cheapest_flight = flight
        return cheapest_flight

from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData

import pprint as pp

# get all data from sheet
dm = DataManager()
dm.initialise_service()
city_list = dm.read_records()

# get the city codes from Tequila API
fs = FlightSearch()
city_codes = fs.get_code_list(city_list)
dm.write_codes(entries=[city_codes])

flights = list()
for each_dest in city_codes:
    each_flight = fs.search_flights(each_dest)
    flight_no = each_flight["route"][0]["flight_no"]
    airline = each_flight["airlines"]
    price = each_flight["price"]
    dep_date = each_flight["utc_departure"]
    dep_airport_code = each_flight["flyFrom"]
    dep_city = each_flight["cityFrom"]
    arr_airport_code = each_flight["flyTo"]
    arr_city = each_flight["cityTo"]
    ticket_link = each_flight["deep_link"]
    flight = FlightData(airline, flight_no, price, dep_date, dep_airport_code,
                        dep_city, arr_airport_code, arr_city, ticket_link)
    flights.append(flight)

for flight in flights:
    print(f"{flight.arrival_city}: €{flight.price}")

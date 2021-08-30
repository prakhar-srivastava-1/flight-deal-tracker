from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

import pprint as pp

# get all data from sheet
dm = DataManager()
dm.initialise_service()
sheet_records = dm.read_records()

# get the city codes from Tequila API
fs = FlightSearch()
city_codes = fs.get_code_list(sheet_records)
# dm.write_codes(entries=[city_codes])

# get the prices mentioned in sheet
prices_from_sheet = dm.get_flight_price(sheet_records)

# create a list of tuples [(city_code, price), ...]
sheet_city_price = dict(zip(city_codes, prices_from_sheet))

flights = list()
# each_flight = fs.search_flights('TYO')
# pp.pprint(each_flight)

for each_dest in city_codes:
    each_flight = fs.search_flights(each_dest, sheet_city_price[each_dest])
    if len(each_flight) != 0:
        each_flight = each_flight[0]
        flight_no = each_flight["route"][0]["flight_no"]
        airline = each_flight["airlines"]
        price = each_flight["price"]
        dep_date = each_flight["route"][0]["utc_departure"]
        dep_airport_code = each_flight["flyFrom"]
        dep_city = each_flight["cityFrom"]
        arr_airport_code = each_flight["flyTo"]
        arr_city = each_flight["cityTo"]
        ticket_link = each_flight["deep_link"]
        # Return journey
        ret_flight_no = each_flight["route"][1]["flight_no"]
        ret_dep_date = each_flight["route"][1]["utc_departure"]

        flight = FlightData(airline, flight_no, price, dep_date, ret_dep_date,
                            dep_airport_code, dep_city, arr_airport_code, arr_city,
                            ticket_link)
        flights.append(flight)
        # print(flights)

cheapest_flight = fs.get_cheapest_flight(flights)

# send a notification if cheapest_flight not None
nm = NotificationManager()
if cheapest_flight is not None:
    nm.send_alert(cheapest_flight)

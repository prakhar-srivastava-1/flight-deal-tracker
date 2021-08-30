from user_data import UserData
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# get all data from sheet
dm = DataManager()
dm.initialise_service()
sheet_records = dm.read_records(sheet_name="prices")

# get the city codes from Tequila API
fs = FlightSearch()
city_codes = fs.get_code_list(sheet_records)
# dm.write_codes(entries=[city_codes])

# get the prices mentioned in sheet
prices_from_sheet = dm.get_flight_price(sheet_records)

# create a list of tuples [(city_code, price), ...]
sheet_city_price = dict(zip(city_codes, prices_from_sheet))

flights = list()

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
print(f"Found the cheapest flight: {cheapest_flight.flight_no}")

# user = UserData()
# user.get_details()
# dm.add_user(user)

# read all records from "users"
users = dm.read_records(sheet_name="users")

# create user objects and send email
user_list = list()

for user in users:
    user = UserData(
        first_name=user[0],
        last_name=user[1],
        email=user[2]
    )
    user_list.append(user)
print(f"All users fetched.")

# send email
nm = NotificationManager()
for each_user in user_list:
    nm.send_email(each_user, cheapest_flight)
print("All users notified!")


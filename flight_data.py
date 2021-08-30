# Will use this class for saving flights and comparison of fares

class FlightData:
    def __init__(self, airline, flight_no, price, dep_date, ret_dep_date, dep_airport_code,
                 dep_city, arr_airport_code, arr_city, ticket_link):
        self.airline = airline
        self.flight_no = flight_no
        self.price = price
        self.departure_date = dep_date
        self.ret_dep_date = ret_dep_date
        self.departure_airport_code = dep_airport_code
        self.departure_city = dep_city
        self.arrival_airport_code = arr_airport_code
        self.arrival_city = arr_city
        self.ticket_link = ticket_link
        self.clean_date()

    def clean_date(self):
        self.ret_dep_date = self.ret_dep_date.split("T")[0]
        self.departure_date = self.departure_date.split("T")[0]

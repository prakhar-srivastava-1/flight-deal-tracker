from secrets import TWILIO_PHONE, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, MY_PHONE
from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:

    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.phone = TWILIO_PHONE
        self.auth_token = TWILIO_AUTH_TOKEN
        self.my_phone = MY_PHONE
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    def send_alert(self, flight: FlightData):
        text_body = f"Only £{flight.price} to fly from " \
                    f"{flight.departure_city}-{flight.departure_airport_code} to " \
                    f"{flight.arrival_city}-{flight.arrival_airport_code}, from " \
                    f"{flight.departure_date} to {flight.ret_dep_date}."
        message = self.client.messages.create(
            body=text_body,
            from_=self.phone,
            to=self.my_phone
        )
        print(message.status)

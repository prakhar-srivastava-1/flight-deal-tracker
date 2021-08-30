from secrets import TWILIO_PHONE, TWILIO_ACCOUNT_SID, \
                    TWILIO_AUTH_TOKEN, MY_PHONE, \
                    EMAIL, EMAIL_PASSWORD
from twilio.rest import Client
from flight_data import FlightData
import smtplib


class NotificationManager:

    def __init__(self):
        self.account_sid = TWILIO_ACCOUNT_SID
        self.phone = TWILIO_PHONE
        self.auth_token = TWILIO_AUTH_TOKEN
        self.my_phone = MY_PHONE
        self.client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        self.email = EMAIL
        self.email_password = EMAIL_PASSWORD

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

    def send_email(self, user, flight):
        email_body = f"Dear {user.first_name} {user.last_name}," \
                     f"Only £{flight.price} to fly from " \
                     f"{flight.departure_city}-{flight.departure_airport_code} to " \
                     f"{flight.arrival_city}-{flight.arrival_airport_code}, from " \
                     f"{flight.departure_date} to {flight.ret_dep_date}."

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.email, password=self.email_password)
            connection.sendmail(from_addr=self.email, to_addrs=user.email,
                                msg=email_body)

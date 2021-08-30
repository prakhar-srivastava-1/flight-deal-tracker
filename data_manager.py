import requests
from secrets import GOOGLE_API_KEY, SPREADSHEET_ENDPOINT, SPREADSHEET_ID
from googleapiclient.discovery import build
from google.oauth2 import service_account

SPREADSHEET_RANGE = "A2:C"


class DataManager:
    def __init__(self):
        self.endpoint_get = self.endpoint_put = SPREADSHEET_ENDPOINT
        self.max_row = 0
        self.service = None

    def initialise_service(self):
        scopes = ['https://www.googleapis.com/auth/spreadsheets']
        service_account_file = 'keys.json'

        # Create credentials for REST call
        creds = service_account.Credentials.from_service_account_file(
            service_account_file,
            scopes=scopes
        )

        # Build the service object
        self.service = build('sheets', 'v4', credentials=creds)

    def read_records(self, sheet_name):
        # Call the Sheets API
        sheet = self.service.spreadsheets()

        result = sheet.values().get(
            spreadsheetId=SPREADSHEET_ID, range=f"{sheet_name}!{SPREADSHEET_RANGE}").execute()
        rows = result.get('values', [])
        return rows

    @staticmethod
    def get_flight_price(records):
        flight_prices = list()
        for city in records:
            flight_prices.append(city[2])
        return flight_prices

    def write_codes(self, entries):
        # Call the Sheets API
        sheet = self.service.spreadsheets()

        # records to write
        records = {
            "values": entries,
            "majorDimension": "COLUMNS",
        }

        request = sheet.values().update(
            spreadsheetId=SPREADSHEET_ID,
            range="B2",
            valueInputOption="USER_ENTERED",
            body=records
        )
        response = request.execute()

        if int(response.get("updatedRows")) > 0:
            return True
        return False

    def add_user(self, user):
        # Call the Sheets API
        sheet = self.service.spreadsheets()

        # create record
        entries = [
            [
                user.first_name,
                user.last_name,
                user.email
            ]
        ]

        # records to write
        records = {
            "values": entries,
            "majorDimension": "ROWS",
        }

        request = sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range="users",
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=records
        )
        response = request.execute()

        if response.get("updatedRange") is not None:
            return True
        return False

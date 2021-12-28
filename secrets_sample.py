# Google Sheets
# pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
SPREADSHEET_ID = "YOUR_SPREADSHEET_ID"

SPREADSHEET_ENDPOINT = f"https://sheets.googleapis.com/v4/spreadsheets/" \
                       f"{SPREADSHEET_ID}/values/"


# Tequila - Flight Search
TEQUILA_API_KEY = "YOUR_TQUILA_API_KEY"
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
TEQUILA_ENDPOINT_FLIGHT = "https://tequila-api.kiwi.com/v2/search"

# Twilio - SMS
TWILIO_PHONE = "YOUR_TWILIO_PHONE_NUMBER"
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
MY_PHONE = "PPHONE_NUMBER_WHERE_YOU_GET_THE_TEXT"

# Email
# NOTE: You may need to update mailbox security settings to allow access from insecure apps
EMAIL = "YOUR_EMAIL"
EMAIL_PASSWORD = "EMAIL_PASSWORD"
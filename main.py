from data_manager import DataManager
from user_data import UserData
from notification_manager import NotificationManager
from flight_data import FlightData

# user = UserData()
# user.get_details()

dm = DataManager()
dm.initialise_service()
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

# send email
nm = NotificationManager()
cheapest_flight = FlightData()
for each_user in user_list:
    nm.send_email(each_user, cheapest_flight)
print(user_list)

from data_manager import DataManager
from user_data import UserData

user = UserData()
user.get_details()

dm = DataManager()
dm.initialise_service()
dm.add_user(user)

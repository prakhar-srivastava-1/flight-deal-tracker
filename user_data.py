class UserData:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.email = ""

    def get_details(self):
        print("Welcome to the Flight Club!\nWe find the best flight deals and email you")
        self.first_name = input("What is your first name?\n")
        self.last_name = input("What is your last name?\n")
        email1 = input("What is your email?\n")
        email2 = input("Type your email again.\n")
        if email1 == email2:
            self.email = email1
            print("You're now in the club!!")
        else:
            print(f"Dear {self.first_name}, your emails did not match. Please try again!")

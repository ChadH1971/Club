# start definition of Renegade class

class Renegade:
    def __init__(self,
                 first_name,
                 last_name
                 ):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


selection = input("Press 1 for new Renegade")
if selection == 1:
    user_name = input("Renegade, please enter a username: ")
    print(f"Thank you, {user_name}")
    f_name = input("What is your first name? ")
    l_name = input("What is your last name? ")

    user_name = Renegade(f_name, l_name)

    print(f"{user_name}'s full name is {user_name.full_name()}")

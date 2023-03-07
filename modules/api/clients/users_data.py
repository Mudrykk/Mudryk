class User:
    """This class is for creating a new user."""
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        """Method to create a user."""
        self.name = "Yurii"
        self.second_name = "Mudryk"

    def remove(self):
        """Method to remove a user"""
        self.name = ""
        self.second_name = ""

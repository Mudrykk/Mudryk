class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Yurii"
        self.second_name = "Mudryk"

    def remove(self):
        self.name = ""
        self.second_name = ""
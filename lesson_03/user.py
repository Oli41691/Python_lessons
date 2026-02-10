class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_Name(self):
        return self.first_name

    def get_LastName(self):
        return self.last_name

    def get_All(self):
        return f"Имя: {self.first_name}, Фамилия: {self.last_name}"

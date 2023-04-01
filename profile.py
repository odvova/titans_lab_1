class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Last Name: {self.last_name}\n"
                f"Phone Number: {self.phone_number}\n"
                f"Address: {self.address}\n"
                f"Email: {self.email}\n"
                f"Birthday: {self.birthday}\n"
                f"Age: {self.age}\n"
                f"Sex: {self.sex}")

from faker import Faker


class Profile:
    def __init__(self):
        self.faker = Faker()
        self.ssn = self.faker.ssn()
        self.name = self.faker.name()
        self.address = self.faker.address()
        self.phone = self.faker.phone_number()
        self.job = self.faker.job()

    def to_json(self):
        return {
            "ssn": self.ssn,
            "name": self.name,
            "address": self.address,
            "phone": self.phone,
            "job": self.job,
        }

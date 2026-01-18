from faker import Faker
from faker.providers.python import TEnum
from shortuuid import uuid



class Fake:
    """
    Class for generating fake data for testing using Faker library.
    """
    def __init__(self, faker: Faker):
        self.faker = faker

    def enum_choice(self, value: type[TEnum]):
        """
        Chooses a random value from a given enum.

        :param value: The enum class to select the random value from.
        :return: A random value selected from the enum.
        """
        return self.faker.enum(value)

    def email(self) -> str:
        """
        Generates a random email address.

        :return: A random email address.
        """
        return f'test_user_{uuid()}.{self.faker.email()}'

    def category(self) -> str:
        """
        Selects a random category name from a category list.

        :return: A random category name.
        """
        return self.faker.random_element(
            [
                "gas",
                "taxi",
                "tolls",
                "water",
                "beauty",
                "mobile",
                "travel",
                "parking",
                "catalog",
                "internet",
                "satellite",
                "education",
                "government",
                "healthcare",
                "restaurants",
                "electricity",
                "supermarkets",
            ]
        )

    def last_name(self) -> str:
        """
        Generates a random last name.

        :return: A random last name.
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Generates a random first name.

        :return: A random first name.
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Generates a random middle name.

        :return: A random middle name.
        """
        return self.faker.middle_name()

    def phone_number(self) -> str:
        """
        Generates a random phone number.

        :return: A random phone number.
        """
        return self.faker.phone_number()

    def float_generator(self, start: int = 1, end: int = 100) -> float:
        """
        Generates a random float number in given range.

        :param start: The start of the range.
        :param end: The end of the range.
        :return: A random float number.
        """
        return self.faker.pyfloat(min_value=start, max_value=end, right_digits=2)

    def amount(self) -> float:
        """
        Generates a random amount within the range of 1 to 1000.

        :return: A random amount.
        """
        return self.float_generator(1, 1000)


fake = Fake(faker=Faker('ru_RU'))

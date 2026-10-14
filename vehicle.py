from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, registration_number, make, model, year, daily_rate):

        if daily_rate < 0:
            raise ValueError("Daily rate cannot be negative.")

        self.registration_number = registration_number
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate
        self.__available = True

    def is_available(self):
        return self.__available

    def mark_as_rented(self):
        self.__available = False

    def mark_as_available(self):
        self.__available = True

    def display_details(self):

        status = "Available" if self.__available else "Rented"

        print(f"Vehicle: {self.make} {self.model}")
        print(f"Registration: {self.registration_number}")
        print(f"Year: {self.year}")
        print(f"Daily Rate: KSh {self.daily_rate:,.0f}")
        print(f"Status: {status}")

    @abstractmethod
    def calculate_rental_cost(self, days):
        pass


class EconomyCar(Vehicle):

    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(
            registration_number,
            make,
            model,
            year,
            daily_rate
        )

    def calculate_rental_cost(self, days):
        return self.daily_rate * days


class SUV(Vehicle):

    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(
            registration_number,
            make,
            model,
            year,
            daily_rate
        )

    def calculate_rental_cost(self, days):
        return (self.daily_rate * days) + 2000


class LuxuryCar(Vehicle):

    def __init__(self, registration_number, make, model, year, daily_rate):
        super().__init__(
            registration_number,
            make,
            model,
            year,
            daily_rate
        )

    def calculate_rental_cost(self, days):

        rental_charge = self.daily_rate * days
        insurance = rental_charge * 0.10

        return rental_charge + insurance
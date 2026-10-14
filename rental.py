class Rental:

    def __init__(self, rental_id, customer, vehicle, rental_days):

        if rental_days <= 0:
            raise ValueError("Rental days must be greater than zero.")

        self.rental_id = rental_id
        self.customer = customer
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.actual_days = None

        self.status = "ACTIVE"

        self.base_cost = vehicle.calculate_rental_cost(rental_days)

        self.late_fee = 0
        self.damage_charge = 0

        self.__paid = False

    def calculate_late_fee(self):

        if self.actual_days is None:
            return 0

        late_days = max(
            0,
            self.actual_days - self.rental_days
        )

        daily_late_penalty = self.vehicle.daily_rate * 0.20

        self.late_fee = daily_late_penalty * late_days

        return self.late_fee

    def calculate_total(self):

        return (
            self.base_cost
            + self.late_fee
            + self.damage_charge
        )

    def complete_rental(self, actual_days, damage_charge=0):

        if self.status == "COMPLETED":
            raise ValueError(
                "Rental has already been completed."
            )

        if self.status == "CANCELLED":
            raise ValueError(
                "Cancelled rental cannot be completed."
            )

        if actual_days <= 0:
            raise ValueError(
                "Actual rental days must be greater than zero."
            )

        if damage_charge < 0:
            raise ValueError(
                "Damage charge cannot be negative."
            )

        self.actual_days = actual_days
        self.damage_charge = damage_charge

        self.calculate_late_fee()

        self.status = "COMPLETED"

    def mark_as_paid(self):
        self.__paid = True

    def is_paid(self):
        return self.__paid

    def display_rental_details(self):

        print("====================================")
        print("        SAFARIDRIVE RENTALS")
        print("====================================")

        print(f"Rental ID:        {self.rental_id}")
        print(f"Customer:         {self.customer.name}")
        print(
            f"Vehicle:          "
            f"{self.vehicle.make} {self.vehicle.model}"
        )
        print(
            f"Registration:     "
            f"{self.vehicle.registration_number}"
        )
        print(f"Rental Period:    {self.rental_days} days")
        print(
            f"Daily Rate:       "
            f"KSh {self.vehicle.daily_rate:,.0f}"
        )

        print()

        print(
            f"Rental Charge:    "
            f"KSh {self.base_cost:,.0f}"
        )

        if self.vehicle.__class__.__name__ == "SUV":
            print("Service Charge:   KSh 2,000")

        elif self.vehicle.__class__.__name__ == "LuxuryCar":

            insurance = (
                self.vehicle.daily_rate
                * self.rental_days
                * 0.10
            )

            print(
                f"Insurance:        "
                f"KSh {insurance:,.0f}"
            )

        if self.late_fee > 0:
            print(
                f"Late Fee:         "
                f"KSh {self.late_fee:,.0f}"
            )

        if self.damage_charge > 0:
            print(
                f"Damage Charge:    "
                f"KSh {self.damage_charge:,.0f}"
            )

        print("------------------------------------")

        print(
            f"TOTAL:            "
            f"KSh {self.calculate_total():,.0f}"
        )

        print(f"Status:           {self.status}")

        print("====================================")
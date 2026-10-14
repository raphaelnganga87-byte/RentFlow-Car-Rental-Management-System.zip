from rental import Rental
from vehicle import EconomyCar, SUV, LuxuryCar


class CarRentalSystem:

    def __init__(self):

        self.name = "SafariDrive Rentals"

        self.vehicles = []
        self.customers = []
        self.rentals = []
        self.payments = []

        self.__revenue = 0

    # ==========================================
    # VEHICLE MANAGEMENT
    # ==========================================

    def add_vehicle(self, vehicle):

        self.vehicles.append(vehicle)

    def find_vehicle(self, registration_number):

        for vehicle in self.vehicles:

            if vehicle.registration_number == registration_number:
                return vehicle

        return None

    def show_available_vehicles(self):

        print("\n--- AVAILABLE VEHICLES ---")

        for vehicle in self.vehicles:

            if vehicle.is_available():
                vehicle.display_details()

    def search_vehicles(
        self,
        vehicle_type=None,
        max_daily_rate=None
    ):

        results = []

        for vehicle in self.vehicles:

            # Only search available vehicles
            if not vehicle.is_available():
                continue

            if vehicle_type is not None:

                if vehicle.__class__.__name__ != vehicle_type:
                    continue

            if max_daily_rate is not None:

                if vehicle.daily_rate > max_daily_rate:
                    continue

            results.append(vehicle)

        return results

    # ==========================================
    # CUSTOMER MANAGEMENT
    # ==========================================

    def register_customer(self, customer):

        self.customers.append(customer)

    def find_customer(self, customer_id):

        for customer in self.customers:

            if customer.customer_id == customer_id:
                return customer

        return None

    # ==========================================
    # RENTAL MANAGEMENT
    # ==========================================

    def rent_vehicle(self, customer, vehicle, days):

        if customer not in self.customers:

            raise ValueError(
                "Customer must be registered before renting."
            )

        if vehicle not in self.vehicles:

            raise ValueError(
                "Vehicle is not in the fleet."
            )

        if not vehicle.is_available():

            raise ValueError(
                "Vehicle is currently unavailable."
            )

        if days <= 0:

            raise ValueError(
                "Rental days must be greater than zero."
            )

        rental_id = f"R{len(self.rentals) + 1:03d}"

        rental = Rental(
            rental_id,
            customer,
            vehicle,
            days
        )

        vehicle.mark_as_rented()

        self.rentals.append(rental)

        customer.add_rental(rental)

        return rental

    def return_vehicle(
        self,
        rental,
        actual_days,
        damage_charge=0
    ):

        if rental not in self.rentals:

            raise ValueError(
                "Rental does not exist in the system."
            )

        if rental.status != "ACTIVE":

            raise ValueError(
                "Vehicle has already been returned."
            )

        # Make sure the vehicle is actually rented
        if rental.vehicle.is_available():

            raise ValueError(
                "Vehicle is not currently rented."
            )

        rental.complete_rental(
            actual_days,
            damage_charge
        )

        rental.vehicle.mark_as_available()

        return rental

    # ==========================================
    # PAYMENT MANAGEMENT
    # ==========================================

    def process_payment(self, payment):

        rental = payment.rental

        if rental not in self.rentals:

            raise ValueError(
                "Rental does not exist in the system."
            )

        if rental.status != "COMPLETED":

            raise ValueError(
                "Rental must be completed before payment."
            )

        if rental.is_paid():

            raise ValueError(
                "Rental has already been paid."
            )

        success = payment.process_payment()

        if success:

            rental.mark_as_paid()

            self.payments.append(payment)

            self.__revenue += payment.amount

        return success

    # ==========================================
    # RENTAL REPORTS
    # ==========================================

    def show_active_rentals(self):

        print("\n--- ACTIVE RENTALS ---")

        for rental in self.rentals:

            if rental.status == "ACTIVE":
                rental.display_rental_details()

    def show_completed_rentals(self):

        print("\n--- COMPLETED RENTALS ---")

        for rental in self.rentals:

            if rental.status == "COMPLETED":
                rental.display_rental_details()

    # ==========================================
    # REVENUE
    # ==========================================

    @property
    def revenue(self):

        return self.__revenue

    # ==========================================
    # MANAGEMENT REPORT
    # ==========================================

    def generate_report(self):

        available_count = 0
        rented_count = 0

        active_count = 0
        completed_count = 0

        economy_count = 0
        suv_count = 0
        luxury_count = 0

        # Count vehicles and categories
        for vehicle in self.vehicles:

            if vehicle.is_available():
                available_count += 1
            else:
                rented_count += 1

            if isinstance(vehicle, EconomyCar):
                economy_count += 1

            elif isinstance(vehicle, SUV):
                suv_count += 1

            elif isinstance(vehicle, LuxuryCar):
                luxury_count += 1

        # Count rentals by status
        for rental in self.rentals:

            if rental.status == "ACTIVE":
                active_count += 1

            elif rental.status == "COMPLETED":
                completed_count += 1

        print("\n====================================")
        print("     SAFARIDRIVE MANAGEMENT REPORT")
        print("====================================")

        print(
            f"Total Vehicles:          "
            f"{len(self.vehicles)}"
        )

        print(
            f"Available Vehicles:      "
            f"{available_count}"
        )

        print(
            f"Rented Vehicles:         "
            f"{rented_count}"
        )

        print(
            f"Registered Customers:    "
            f"{len(self.customers)}"
        )

        print(
            f"Total Rentals:           "
            f"{len(self.rentals)}"
        )

        print(
            f"Total Payments:          "
            f"{len(self.payments)}"
        )

        print(
            f"Active Rentals:          "
            f"{active_count}"
        )

        print(
            f"Completed Rentals:       "
            f"{completed_count}"
        )

        print(
            f"Total Revenue:           "
            f"KSh {self.__revenue:,.0f}"
        )

        print()
        print("VEHICLES BY CATEGORY")

        print(
            f"Economy Cars:            "
            f"{economy_count}"
        )

        print(
            f"SUVs:                    "
            f"{suv_count}"
        )

        print(
            f"Luxury Cars:             "
            f"{luxury_count}"
        )

        print("====================================")
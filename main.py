from vehicle import EconomyCar, SUV, LuxuryCar
from customer import Customer
from payment import MpesaPayment, CardPayment, CashPayment
from rental_system import CarRentalSystem


# ==========================================
# SAFARIDRIVE RENTALS
# MAIN TEST PROGRAM
# ==========================================

print("====================================")
print("        SAFARIDRIVE RENTALS")
print("====================================")


# ==========================================
# 1. CREATE RENTAL SYSTEM
# ==========================================

system = CarRentalSystem()


# ==========================================
# 2. CREATE CUSTOMERS
# ==========================================

customer1 = Customer(
    "C001",
    "John Kamau",
    "0712345678",
    "12345678",
    "DL45821"
)

customer2 = Customer(
    "C002",
    "Mary Wanjiku",
    "0723456789",
    "23456789",
    "DL56234"
)

customer3 = Customer(
    "C003",
    "Peter Otieno",
    "0734567890",
    "34567890",
    "DL67345"
)

system.register_customer(customer1)
system.register_customer(customer2)
system.register_customer(customer3)


# ==========================================
# 3. CREATE 5 VEHICLES
# ==========================================

economy1 = EconomyCar(
    "KDA 101A",
    "Toyota",
    "Vitz",
    2022,
    3500
)

economy2 = EconomyCar(
    "KDB 202B",
    "Honda",
    "Fit",
    2023,
    4000
)

suv1 = SUV(
    "KDJ 456B",
    "Toyota",
    "Prado",
    2023,
    8000
)

suv2 = SUV(
    "KDK 789C",
    "Nissan",
    "X-Trail",
    2022,
    6500
)

luxury1 = LuxuryCar(
    "KDL 321D",
    "Mercedes",
    "E-Class",
    2024,
    15000
)

system.add_vehicle(economy1)
system.add_vehicle(economy2)
system.add_vehicle(suv1)
system.add_vehicle(suv2)
system.add_vehicle(luxury1)


# ==========================================
# 4. SHOW AVAILABLE VEHICLES
# ==========================================

print("\n--- AVAILABLE VEHICLES ---")

system.show_available_vehicles()


# ==========================================
# 5. CREATE RENTALS
# ==========================================

print("\n--- RENTING VEHICLES ---")

rental1 = system.rent_vehicle(
    customer1,
    suv1,
    4
)

print("Rental 1 created successfully.")


rental2 = system.rent_vehicle(
    customer2,
    economy1,
    3
)

print("Rental 2 created successfully.")


rental3 = system.rent_vehicle(
    customer3,
    luxury1,
    2
)

print("Rental 3 created successfully.")


# ==========================================
# 6. SHOW ACTIVE RENTALS
# ==========================================

system.show_active_rentals()


# ==========================================
# 7. RETURN RENTAL 1
# ==========================================

print("\n--- RETURNING RENTAL 1 ---")

system.return_vehicle(
    rental1,
    actual_days=5
)

rental1.display_rental_details()


# ==========================================
# 8. RETURN RENTAL 2 WITH DAMAGE
# ==========================================

print("\n--- RETURNING RENTAL 2 WITH DAMAGE ---")

system.return_vehicle(
    rental2,
    actual_days=3,
    damage_charge=5000
)

rental2.display_rental_details()


# ==========================================
# 9. PAYMENT FOR RENTAL 1
# ==========================================

print("\n--- PAYMENT FOR RENTAL 1 ---")

payment1 = MpesaPayment(
    rental1,
    "0712345678"
)

system.process_payment(payment1)


# ==========================================
# 10. PAYMENT FOR RENTAL 2
# ==========================================

print("\n--- PAYMENT FOR RENTAL 2 ---")

payment2 = CashPayment(
    rental2,
    50000
)

system.process_payment(payment2)


# ==========================================
# 11. SEARCH VEHICLES
# ==========================================

print("\n--- SEARCH: SUV VEHICLES ---")

suv_results = system.search_vehicles(
    vehicle_type="SUV"
)

for vehicle in suv_results:
    vehicle.display_details()


print("\n--- SEARCH: VEHICLES BELOW KSh 7,000 ---")

rate_results = system.search_vehicles(
    max_daily_rate=7000
)

for vehicle in rate_results:
    vehicle.display_details()


# ==========================================
# 12. SHOW COMPLETED RENTALS
# ==========================================

system.show_completed_rentals()


# ==========================================
# 13. SHOW AVAILABLE VEHICLES AFTER RENTALS
# ==========================================

system.show_available_vehicles()


# ==========================================
# 14. FINAL REPORT
# ==========================================

print("\n--- FINAL SYSTEM REPORT ---")

system.generate_report()
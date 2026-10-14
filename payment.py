from abc import ABC, abstractmethod
import random
import string


class Payment(ABC):

    def __init__(self, rental):

        self.rental = rental
        self.amount = rental.calculate_total()

        if self.amount < 0:
            raise ValueError(
                "Payment amount cannot be negative."
            )

    @abstractmethod
    def process_payment(self):
        pass


class MpesaPayment(Payment):

    def __init__(self, rental, phone_number):

        super().__init__(rental)

        self.phone_number = phone_number

    def process_payment(self):

        transaction_code = (
            "T"
            + "".join(
                random.choices(
                    string.ascii_uppercase
                    + string.digits,
                    k=9
                )
            )
        )

        print("M-Pesa Payment Successful")
        print(
            f"Phone Number: {self.phone_number}"
        )
        print(
            f"Amount Paid: KSh {self.amount:,.0f}"
        )
        print(
            f"Transaction Code: {transaction_code}"
        )

        return True


class CardPayment(Payment):

    def __init__(self, rental, card_number):

        super().__init__(rental)

        self.last_four_digits = card_number[-4:]

    def process_payment(self):

        print("Card Payment Successful")
        print(
            f"Card: ****{self.last_four_digits}"
        )
        print(
            f"Amount Paid: KSh {self.amount:,.0f}"
        )

        return True


class CashPayment(Payment):

    def __init__(self, rental, cash_amount):

        super().__init__(rental)

        if cash_amount < 0:
            raise ValueError(
                "Cash amount cannot be negative."
            )

        self.cash_amount = cash_amount

    def process_payment(self):

        if self.cash_amount < self.amount:

            print("Payment Failed")
            print("Insufficient cash.")

            return False

        change = self.cash_amount - self.amount

        print("Cash Payment Successful")

        print(
            f"Amount Paid: KSh {self.amount:,.0f}"
        )

        print(
            f"Cash Received: "
            f"KSh {self.cash_amount:,.0f}"
        )

        print(
            f"Change: KSh {change:,.0f}"
        )

        return True
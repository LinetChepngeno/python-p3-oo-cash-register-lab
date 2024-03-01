#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        # Set the discount percentage
        self.discount = discount
        # Initialize the total amount
        self.total = 0
        # Initialize the list of items
        self.items = []
        # Initialize the list of previous transactions
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # Update the total amount
        self.total += price * quantity
        for _ in range(quantity):
            # Add the item to the list of items
            self.items.append(item)
             # Add the transaction to the list of previous transactions
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

     # Apply the discount
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        # Subtract the last transaction from the total
        self.total -= (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        for _ in range(self.previous_transactions[-1]["quantity"]):
            # Remove the item from the list of items
            self.items.pop()
            # Remove the transaction from the list of previous transactions
        self.previous_transactions.pop()
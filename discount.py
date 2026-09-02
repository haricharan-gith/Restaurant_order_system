from abc import ABC, abstractmethod


class Discount(ABC):
    """Abstract discount strategy — apply() takes a subtotal, returns the amount to subtract."""

    @abstractmethod
    def apply(self, subtotal):
        raise NotImplementedError

    @abstractmethod
    def describe(self):
        raise NotImplementedError


class PercentageDiscount(Discount):
    def __init__(self, percent):
        if not (0 <= percent <= 100):
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply(self, subtotal):
        return round(subtotal * (self.percent / 100), 2)

    def describe(self):
        return f"{self.percent}% off"


class FlatDiscount(Discount):
    def __init__(self, amount):
        if amount < 0:
            raise ValueError("Discount amount cannot be negative.")
        self.amount = amount

    def apply(self, subtotal):
        return min(self.amount, subtotal)  # never discount below zero

    def describe(self):
        return f"₹{self.amount:.2f} off"


class NoDiscount(Discount):
    def apply(self, subtotal):
        return 0.0

    def describe(self):
        return "No discount"

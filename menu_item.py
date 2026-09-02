from abc import ABC, abstractmethod


class MenuItem(ABC):
    """Abstract base class for any item on the menu.

    Encapsulation: the price is stored as a "private" attribute
    (name-mangled with a double underscore) and only ever exposed
    or changed through methods/properties — never touched directly.
    """

    def __init__(self, name, price):
        self._name = name
        self.__price = self._validate_price(price)

    @staticmethod
    def _validate_price(price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        return round(price, 2)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = self._validate_price(new_price)

    @abstractmethod
    def category(self):
        """Each subclass must say what category it belongs to."""
        raise NotImplementedError

    def describe(self):
        return f"{self.name} ({self.category()}) — ₹{self.price:.2f}"

    def __repr__(self):
        return f"<{self.__class__.__name__} '{self.name}' ₹{self.price:.2f}>"


class Appetizer(MenuItem):
    def category(self):
        return "Appetizer"


class MainCourse(MenuItem):
    def __init__(self, name, price, is_vegetarian=False):
        super().__init__(name, price)
        self.is_vegetarian = is_vegetarian

    def category(self):
        return "Main Course"

    def describe(self):
        tag = " (Veg)" if self.is_vegetarian else ""
        return f"{self.name}{tag} ({self.category()}) — ₹{self.price:.2f}"


class Dessert(MenuItem):
    def category(self):
        return "Dessert"


class Beverage(MenuItem):
    def category(self):
        return "Beverage"

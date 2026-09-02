from menu_item import Appetizer, MainCourse, Dessert, Beverage


class Menu:
    """Holds all available MenuItems the restaurant offers."""

    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def list_items(self):
        return list(self._items)  # return a copy, not the internal list

    def find_by_name(self, name):
        for item in self._items:
            if item.name.lower() == name.lower():
                return item
        return None

    def display(self):
        print("\n===== MENU =====")
        for i, item in enumerate(self._items, start=1):
            print(f"  {i}. {item.describe()}")
        print("================\n")


def build_sample_menu():
    """Convenience factory — a ready-made menu for demos/tests."""
    menu = Menu()
    menu.add_item(Appetizer("Spring Rolls", 149.00))
    menu.add_item(Appetizer("Garlic Bread", 120.00))
    menu.add_item(MainCourse("Grilled Chicken", 349.00))
    menu.add_item(MainCourse("Paneer Tikka Masala", 299.00, is_vegetarian=True))
    menu.add_item(MainCourse("Veg Biryani", 249.00, is_vegetarian=True))
    menu.add_item(Dessert("Chocolate Lava Cake", 159.00))
    menu.add_item(Dessert("Gulab Jamun", 89.00))
    menu.add_item(Beverage("Iced Tea", 69.00))
    menu.add_item(Beverage("Mango Lassi", 89.00))
    return menu

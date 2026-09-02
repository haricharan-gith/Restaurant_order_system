from menu import build_sample_menu
from order import Order
from discount import PercentageDiscount, FlatDiscount, NoDiscount


def choose_discount():
    print("\nApply a discount?")
    print("  1. None")
    print("  2. Percentage off")
    print("  3. Flat amount off")
    choice = input("Choose (1-3): ").strip()

    if choice == "2":
        try:
            percent = float(input("Percent off: "))
            return PercentageDiscount(percent)
        except ValueError:
            print("Invalid input — no discount applied.")
    elif choice == "3":
        try:
            amount = float(input("Amount off (₹): "))
            return FlatDiscount(amount)
        except ValueError:
            print("Invalid input — no discount applied.")

    return NoDiscount()


def main():
    menu = build_sample_menu()
    name = input("Customer name: ").strip() or "Guest"
    order = Order(customer_name=name)

    while True:
        menu.display()
        choice = input("Enter item number to add (or 'done' to finish): ").strip()

        if choice.lower() == "done":
            break

        try:
            index = int(choice) - 1
            item = menu.list_items()[index]
        except (ValueError, IndexError):
            print("Invalid selection. Try again.\n")
            continue

        try:
            qty = input(f"Quantity of {item.name} [1]: ").strip()
            qty = int(qty) if qty else 1
            order.add_item(item, quantity=qty)
            print(f"Added {qty} x {item.name}.\n")
        except ValueError:
            print("Invalid quantity. Item not added.\n")

    if len(order) == 0:
        print("No items ordered. Exiting.")
        return

    order.set_discount(choose_discount())
    print(order.receipt())


if __name__ == "__main__":
    main()

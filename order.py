from discount import NoDiscount


class Order:
    """An order is COMPOSED of MenuItem objects — it doesn't inherit from
    MenuItem, it just holds a collection of them (composition, not inheritance).
    """

    def __init__(self, customer_name, tax_rate=0.08):
        self.customer_name = customer_name
        self._items = []              # list of (MenuItem, quantity) tuples
        self._tax_rate = tax_rate
        self._discount = NoDiscount()

    # ---------- managing items ----------

    def add_item(self, item, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be at least 1.")
        for i, (existing_item, qty) in enumerate(self._items):
            if existing_item.name == item.name:
                self._items[i] = (existing_item, qty + quantity)
                return
        self._items.append((item, quantity))

    def remove_item(self, item_name):
        self._items = [(i, q) for (i, q) in self._items if i.name.lower() != item_name.lower()]

    def set_discount(self, discount):
        self._discount = discount

    # ---------- calculations ----------

    def subtotal(self):
        return round(sum(item.price * qty for item, qty in self._items), 2)

    def discount_amount(self):
        return round(self._discount.apply(self.subtotal()), 2)

    def tax_amount(self):
        taxable = self.subtotal() - self.discount_amount()
        return round(taxable * self._tax_rate, 2)

    def total(self):
        return round(self.subtotal() - self.discount_amount() + self.tax_amount(), 2)

    # ---------- display ----------

    def receipt(self):
        lines = []
        lines.append(f"\n===== Receipt for {self.customer_name} =====")
        for item, qty in self._items:
            line_total = item.price * qty
            lines.append(f"  {qty} x {item.name:<25} ₹{line_total:>7.2f}")
        lines.append("-" * 42)
        lines.append(f"  {'Subtotal':<27} ₹{self.subtotal():>7.2f}")
        if self.discount_amount() > 0:
            lines.append(f"  {'Discount (' + self._discount.describe() + ')':<27} -₹{self.discount_amount():>6.2f}")
        lines.append(f"  {'Tax (' + str(int(self._tax_rate * 100)) + '%)':<27} ₹{self.tax_amount():>7.2f}")
        lines.append("=" * 42)
        lines.append(f"  {'TOTAL':<27} ₹{self.total():>7.2f}")
        lines.append("=" * 42 + "\n")
        return "\n".join(lines)

    def __len__(self):
        return sum(qty for _, qty in self._items)

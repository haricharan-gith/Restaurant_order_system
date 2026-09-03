# Restaurant Order System

A Python-based restaurant order management system demonstrating core Object-Oriented Programming (OOP) principles — abstraction, encapsulation, inheritance, composition, and polymorphism — through a practical, real-world domain: taking and pricing customer orders at a restaurant.

## Project Overview

This project simulates a simplified restaurant ordering workflow. Customers can build an order from a menu of items across multiple categories (appetizers, main courses, desserts, beverages), and the system calculates the final bill by applying discounts where applicable. The project was built as an academic exercise to demonstrate clean OOP design in Python — using abstract base classes, encapsulated attributes, and composed objects instead of a flat, procedural structure.

## Features

- **Menu management** — organize items into categories (Appetizer, Main Course, Dessert, Beverage), each with its own attributes and pricing behavior.
- **Order building** — compose an order from multiple menu items and compute totals[cite: 1].
- **Flexible discounting** — apply different discount strategies (percentage-based, flat-amount, or no discount) to an order without changing the order logic itself[cite: 1].
- **Encapsulated pricing** — item prices are protected behind getter/setter properties to prevent invalid values (e.g. negative prices)[cite: 1].
- **Extensible design** — new menu categories or discount types can be added by subclassing existing abstract base classes, with no changes needed to existing code[cite: 1].

## Tech Stack

- **Language:** Python 3 (standard library only — no external dependencies)[cite: 1]
- **Paradigm:** Object-Oriented Programming[cite: 1]
  - Abstraction — `MenuItem` and `Discount` abstract base classes define required behavior for all subclasses[cite: 1].
  - Inheritance — `Appetizer`, `MainCourse`, `Dessert`, `Beverage` extend `MenuItem`; `PercentageDiscount`, `FlatDiscount`, `NoDiscount` extend `Discount`[cite: 1].
  - Encapsulation — private price attribute exposed via a property getter/setter[cite: 1].
  - Composition — `Order` holds a collection of `MenuItem` objects rather than inheriting from them[cite: 1].
  - Polymorphism — each subclass implements shared methods (e.g. price calculation, discount application) in its own way, called uniformly through the base class interface[cite: 1].

## Project Structure
## Setup & Run Instructions

**Requirements:** Python 3.8 or higher (no external packages required)[cite: 1].

1. Clone the repository:
   ```bash
   git clone [https://github.com/haricharan-gith/Restaurant_order_system.git](https://github.com/haricharan-gith/Restaurant_order_system.git)
   cd Restaurant_order_system
   No virtual environment or `pip install` step is required, since the project uses only the Python standard library.

## Environment Variables

None. This project does not require any environment variables, API keys, or configuration files to run.

## API / Database Notes

This project does not connect to any external API or database. All menu and order data is defined and held in memory (in Python objects) for the duration of the program's execution — no persistence layer is included.

## Team Member Contributions

| Name | Contribution |
|------|--------------|
| Hari Charan | _[e.g. Designed and implemented `menu_item.py` and `menu.py`; menu category classes]_ |
| Kishore | _[e.g. Designed and implemented `order.py` and `discount.py`; discount strategy logic]_ |
| Tharun | _[e.g. Implemented `main.py`, integration testing, and README documentation]_ |

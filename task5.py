import math


def unit_price_per_sqm(diameter, price):
    """
    Calculates the unit price of a pizza per square meter.

    Args:
    diameter (float): Diameter of the pizza in centimeters.
    price (float): Price of the pizza in euros.

    Returns:
    float: Unit price per square meter in euros.
    """
    radius = diameter / 2
    area_cm2 = math.pi * radius ** 2
    area_m2 = area_cm2 / 10000
    return price / area_m2 if area_m2 > 0 else float('inf')


# Main program
if __name__ == "__main__":
    # Input for first pizza
    diameter1 = float(input("Enter the diameter of the first pizza in cm: "))
    price1 = float(input("Enter the price of the first pizza in euros: "))

    # Input for second pizza
    diameter2 = float(input("Enter the diameter of the second pizza in cm: "))
    price2 = float(input("Enter the price of the second pizza in euros: "))

    # Calculate unit prices
    unit_price1 = unit_price_per_sqm(diameter1, price1)
    unit_price2 = unit_price_per_sqm(diameter2, price2)

    #
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")
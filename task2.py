def gallons_to_liters(gallons):
    return gallons * 3.78541
def main():
    print("Enter volumes in US gallons (negative value to exit).")
    while True:
        try:
            user_input = float(input("Enter volume in gallons: "))
            if user_input < 0:
                print("Exiting program.")
                break
            liters = gallons_to_liters(user_input)
            print(f"{user_input} US gallons = {liters:.2f} liters\n")
        except ValueError:
            print("Invalid input. Please enter a numeric value.\n")

if __name__ == "__main__":
    main()
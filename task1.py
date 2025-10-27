import random
def roll_dice():
 dice=random.randint(1, 6)
 return dice
def main():
    result = 0
    while result != 6:
        result = roll_dice()
        print("You rolled:", result)
if __name__ == "__main__":
    main()
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5]
    result = sum_of_list(test_list)
    print(f"The sum of the list {test_list} is: {result}")
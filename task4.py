def remove_odd_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
if __name__ == "__main__":
    test_list = [1, 2, 3, 4, 5, 6, 7, 8]
    even_list = remove_odd_numbers(test_list)
    print(f"Original list: {test_list}")
    print(f"List with odd numbers removed: {even_list}")
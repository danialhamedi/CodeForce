def sum_of_digits(number):
    # Initialize the sum
    digit_sum = 0
    while number > 0:
        # Get the rightmost digit
        digit_sum += number % 10
        # Remove the rightmost digit
        number //= 10
    return digit_sum


# Input: Number of test cases
t = int(input())
for _ in range(t):
    # Input: Largest number Vladislav writes
    n = int(input())
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += sum_of_digits(i)
    print(total_sum)

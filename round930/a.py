# Function to solve a single test case
def solve_test_case(n, grid):
    # Initialize variables to store the lexicographically smallest string and the count of paths
    smallest_string = ""
    path_count = 1

    # Initialize current position
    i, j = 0, 0

    # Traverse the grid
    while i < 2 and j < n:
        # Check if we can move right
        if j < n - 1 and grid[i][j + 1] == "0":
            smallest_string += "0"
            j += 1
        # Otherwise, move down
        else:
            smallest_string += "1"
            i += 1

        # If we are at the bottom-right cell, break the loop
        if i == 1 and j == n - 1:
            break

    # Count the number of zeros in the rest of the grid
    remaining_zeros = sum(row[j + 1 :].count("0") for row in grid)

    # Update path count based on remaining zeros
    for ch in smallest_string:
        if ch == "0":
            path_count *= remaining_zeros
            remaining_zeros -= 1

    return smallest_string, path_count


# Function to solve all test cases
def solve():
    # Read the number of test cases
    t = int(input())

    # Iterate through each test case
    for _ in range(t):
        # Read input for the test case
        n = int(input())
        grid = [input() for _ in range(2)]

        # Solve the test case
        result = solve_test_case(n, grid)

        # Print the result for the test case
        print(result[0])
        print(result[1])


# Call the solve function to run the solution
solve()

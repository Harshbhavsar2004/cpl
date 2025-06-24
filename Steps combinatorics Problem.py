"""
Problem: Pascal's Triangle Generation (Combinatorics)
Generate and print the first n rows of Pascal's Triangle, stopping early if any number exceeds 10^60.

Input:
- An integer n, the number of rows to print.

Output:
- The first n rows of Pascal's Triangle, or stop early if a number exceeds 10^60.

Sample Input:
5

Sample Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Explanation:
Each row is constructed by summing adjacent numbers from the previous row. The process stops if any number in a row exceeds 10^60.

Time Complexity: O(n^2), where n is the number of rows.
Space Complexity: O(n), for storing each row.
"""

def generate_pascals_triangle(rows):
    LIMIT = 10**60
    row = [1]
    for _ in range(rows):
        print(' '.join(str(x) for x in row))
        # Generate next row
        new_row = [1]
        for i in range(1, len(row)):
            new_val = row[i-1] + row[i]
            # If number exceeds limit, still print current row but stop further generation
            if new_val >= LIMIT:
                new_row.append(new_val)
                break
            new_row.append(new_val)
        else:
            new_row.append(1)
        row = new_row
        # Stop early if any number in the new row reached/exceeded limit
        if any(x >= LIMIT for x in row):
            break

def main():
    while True:
        try:
            n = int(input("Enter the number of rows to print: "))
            if n <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    generate_pascals_triangle(n)

if __name__ == "__main__":
    main()
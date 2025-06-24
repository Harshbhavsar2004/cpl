# -------------------------------------------------------------
# 💡 Problem Explanation:
# Given a number `n`, perform the following:
# 1. Reverse the digits of `n` (e.g., 195 → 591)
# 2. Add the reversed number to `n`
# 3. Repeat until the result is a palindrome (same forwards and backwards)
# 4. Return the number of steps and the resulting palindrome

# 📥 Sample Input:
# 3
# 195
# 265
# 750

# 📤 Sample Output:
# 4 9339
# 5 45254
# 3 6666

# 🔍 Explanation:
# - 195 → 786 → 1473 → 5214 → 9339 (4 steps)
# - 265 → 827 → 1555 → 7106 → 13123 → 45254 (5 steps)
# - 750 → 807 → 1515 → 6666 (3 steps)

# -------------------------------------------------------------

def is_palindrome(n):
    # Returns True if `n` is a palindrome
    return str(n) == str(n)[::-1]

def reverse_and_add(n):
    # Repeatedly reverse and add until `n` becomes a palindrome
    count = 0
    while not is_palindrome(n):
        rev = int(str(n)[::-1])  # Reverse the number
        n += rev                # Add reversed number to original
        count += 1             # Increment step count
    return count, n  # Return total steps and resulting palindrome

def main():
    try:
        N = int(input("Enter number of test cases (1 to 100): "))
        if not (0 < N <= 100):
            print("Invalid input. N must be between 1 and 100.")
            return

        print("Enter each number to compute its palindrome:")
        for _ in range(N):
            P = int(input())  # Read the number
            count, palindrome = reverse_and_add(P)
            print(f"{count} {palindrome}")  # Output steps and final result

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

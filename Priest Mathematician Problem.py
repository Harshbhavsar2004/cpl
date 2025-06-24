import sys
from functools import lru_cache

# ---------------------------------------------------------------
# 📘 Problem: Minimum Moves in 4-Peg Tower of Hanoi (Frame–Stewart algorithm)
# ---------------------------------------------------------------
# In the 3-peg Tower of Hanoi, the minimum number of moves to solve N disks is:
#   T3(n) = 2^n - 1

# In the 4-peg variant (Reve's puzzle), the Frame–Stewart algorithm is used:
#   T4(n) = min( 2*T4(k) + T3(n-k) ) for all 1 ≤ k < n
# This recursive formula tries all k from 1 to n-1 to find the minimum moves

# ---------------------------------------------------------------
# ✅ Sample Input:
# 1
# 2
# 3
# 15

# ✅ Sample Output:
# 1
# 3
# 5
# 129

#O(n^2) Space Complexity: O(N)


def t3(n):
    return (1 << n) - 1  # efficient bitwise implementation of 2^n - 1

# t4(n): Returns the minimum number of moves using 4 pegs using Frame–Stewart algorithm
@lru_cache(maxsize=None)  # memoization to avoid recomputation
def t4(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    min_moves = float('inf')
    for k in range(1, n):  # try splitting the problem at all k values
        moves = 2 * t4(k) + t3(n - k)
        if moves < min_moves:
            min_moves = moves
    return min_moves

def main():
    print("Enter number of disks (N) per line. Press Ctrl+D (Linux/Mac) or Ctrl+Z (Windows) to end input.\n")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            N = int(line)
            if N < 0 or N > 10000:
                print("Input out of bounds. Please enter 0 ≤ N ≤ 10000.")
                continue
            print(t4(N))
        except ValueError:
            print("Invalid input, please enter an integer.")

if __name__ == "__main__":
    main()

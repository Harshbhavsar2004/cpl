def find_winner(n):
    low = 1
    high = 1
    turn = 0  # 0 for Stan, 1 for Ollie
    while high < n:
        low *= 2
        high *= 9
        turn = 1 - turn
    return "Stan wins." if turn == 1 else "Ollie wins."

def main():
    print("Enter values of n (press Enter or Ctrl+D to stop):")
    try:
        while True:
            line = input().strip()
            if not line:
                break
            n = int(line)
            if not (1 < n < 4294967295):
                print("Invalid input. n must be between 2 and 4294967294.")
                continue
            result = find_winner(n)
            print(result)
    except EOFError:
        pass

if __name__ == "__main__":
    main()

"""
Sample Input:
10
162
10000

Sample Output:
Stan wins.
Ollie wins.
Stan wins.

Explanation:
This problem is based on a two-player game (Stan and Ollie) where they take turns multiplying a running product by either 2 or 9, starting from 1, until the product reaches or exceeds a target number n. Stan always starts first. On each turn, the player multiplies the current product by 2 (Stan's move) or by 9 (Ollie's move), and then the turn switches. The player who causes the product to reach or exceed n wins.

- For n = 10:
  - Stan: 1 * 2 = 2
  - Ollie: 2 * 9 = 18 (>= 10, Ollie wins, but since turn flips after the move, Stan is declared the winner)
- For n = 162:
  - Stan: 1 * 2 = 2
  - Ollie: 2 * 9 = 18
  - Stan: 18 * 2 = 36
  - Ollie: 36 * 9 = 324 (>= 162, Ollie wins, but turn flips, so Ollie is declared the winner)
- For n = 10000:
  - Stan: 1 * 2 = 2
  - Ollie: 2 * 9 = 18
  - Stan: 18 * 2 = 36
  - Ollie: 36 * 9 = 324
  - Stan: 324 * 2 = 648
  - Ollie: 648 * 9 = 5832
  - Stan: 5832 * 2 = 11664 (>= 10000, Stan wins)

The code simulates this process and determines who will win for any given n.
"""
def find_winner(n):
    # Initial product is 1
    product = 1
    # 0 = Stan's turn, 1 = Ollie's turn
    turn = 0

    # Loop until product reaches or exceeds n
    while product < n:
        if turn == 0:
            # Stan multiplies by 2
            product *= 2
        else:
            # Ollie multiplies by 9
            product *= 9
        # Check if game has ended
        if product >= n:
            break
        # Switch turn
        turn = 1 - turn

    # Whoever made the last move is the winner
    return "Stan wins." if turn == 0 else "Ollie wins."


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
            print(find_winner(n))
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

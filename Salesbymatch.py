"""
Problem: Sock Merchant
Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are, and how many socks are left without a pair.

Input:
- The first line contains an integer n, the number of socks.
- The next n lines each contain an integer representing the color of a sock.

Output:
- The number of pairs of socks.
- The number of leftover socks.

Sample Input:
5
10
20
20
10
30

Sample Output:
Number of pairs: 2
Leftover socks: 1

Explanation:
There are two pairs: (10,10) and (20,20). The sock with color 30 is leftover.

Time Complexity: O(n), where n is the number of socks.
Space Complexity: O(k), where k is the number of unique sock colors.
"""

def sockMerchant(n, ar):
    sock_count = {}
    pairs = 0
    leftovers = 0
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

    for sock, count in sock_count.items():
        pairs += count // 2
        if count % 2 != 0:
            leftovers += 1

    return pairs, leftovers

n = int(input("How Many Socks are there: "))
ar = []
for i in range(n):
    if i == 0:
        print("Enter the Socks Number: ")
    sock = int(input())
    ar.append(sock)
pairs, leftovers = sockMerchant(n, ar)
print(f"Number of pairs: {pairs}")
print(f"Leftover socks: {leftovers}")
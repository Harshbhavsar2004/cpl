"""
Problem: Keyboard Row Words (QWERTY Problem)
Given a list of words, return the words that can be typed using letters of only one row on a standard QWERTY keyboard.

Input:
- A single line containing words separated by spaces.

Output:
- A list of words that can be typed using one row of the keyboard.

Sample Input:
Hello Alaska Dad Peace

Sample Output:
['Alaska', 'Dad']

Explanation:
'Alaska' and 'Dad' can be typed using only the middle row of the keyboard. 'Hello' and 'Peace' require letters from multiple rows.

Time Complexity: O(n * m), where n is the number of words and m is the average length of a word.
Space Complexity: O(n), for storing the result list.
"""

class Solution(object):
    def findWords(self, words):
        # Step 1: Map each character to its keyboard row
        m = {}
        for c in "qwertyuiop":
            m[c] = 1
        for c in "asdfghjkl":
            m[c] = 2
        for c in "zxcvbnm":
            m[c] = 3

        print("Keyboard row mapping:", m)

        ans = []
        for w in words:
            lw = w.lower()
            # Find the first alphabetic character to determine the row
            first_alpha = next((ch for ch in lw if ch.isalpha()), None)
            if first_alpha is None:
                continue  # Skip words with no alphabetic characters
            r = m[first_alpha]
            print(f"\nChecking word: {w} (row {r})")
            # Check if all alphabetic characters are from the same row
            if all(not ch.isalpha() or m[ch] == r for ch in lw):
                print(f" All letters in '{w}' are in row {r}")
                ans.append(w)
            else:
                print(f" Letters in '{w}' are from multiple rows")
        return ans

# Take user input
user_input = input("Enter words separated by space: ")
words = user_input.split()

# Solve and show results
sol = Solution()
result = sol.findWords(words)

print("\nWords that can be typed using letters from one row of the keyboard:")
print(result)
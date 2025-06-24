import sys
from collections import defaultdict
from copy import copy
import string

ALPHABET = string.ascii_lowercase

def load_num():
    return int(sys.stdin.readline().rstrip())

def valid_sub(enc, word, subs):
    """Check if the current substitution mapping can transform
    the encrypted word `enc` to the dictionary word `word`.
    If a mismatch occurs, return False.
    """
    if len(enc) != len(word):
        return False

    for e, w in zip(enc, word):
        if subs[e] and subs[e] != w: 
            return False

    return True

def create_sub(enc, word, subs):
    """Attempt to extend the current substitution mapping so that
    `enc` can map to `word`. If the substitution is invalid, raise ValueError.
    """
    new_subs = copy(subs)

    for e, w in zip(enc, word):
        if new_subs[e] == w:
            continue

        if new_subs[e] is not None:
            raise ValueError

        # Ensure no two letters are mapped to the same target letter
        if w in new_subs.values():
            raise ValueError
        new_subs[e] = w
    
    return new_subs

def decrypt(enc, words, subs=None):
    """Recursive decryption using backtracking.
    Tries to decode each word from the encrypted sentence.
    """
    if subs is None:
        subs = {c: None for c in ALPHABET}

    for word in words[len(enc[0])]:
        # Check if the word is consistent with the current substitutions
        if not valid_sub(enc[0], word, subs):
            continue

        # Try to extend the substitution
        try:
            new_subs = create_sub(enc[0], word, subs)
        except ValueError:
            continue
 
        # If it's the last encrypted word, return the result
        if len(enc) == 1:
            return [word]
        
        # Otherwise, recurse on the rest of the sentence
        dec = decrypt(enc[1:], words, new_subs)
        if dec is not None:
            return [word] + dec
        
    return None

if __name__ == '__main__':
    nwords = load_num()
    
    words = defaultdict(list)
    for _ in range(nwords):
        word = sys.stdin.readline().rstrip().lower()
        words[len(word)].append(word)

    for enc in sys.stdin:
        enc = enc.split()
        if len(enc) == 0:
            break

        dec = decrypt(enc, words)
        if dec:
            print(' '.join(dec))
        else:        
            print(' '.join("*"*len(w) for w in enc))

"""
# -------------------------------------------------------------
# 📘 Problem Explanation:
# -------------------------------------------------------------
# You are given a dictionary of lowercase words and several encrypted sentences.
# Each sentence contains words with the same letter-substitution cipher.
# Your task is to decode the sentence using the dictionary or print '*' if no solution is found.

# -------------------------------------------------------------
# ✅ Sample Input:
# (Suppose this is piped via stdin)

6
and
dick
jane
puff
spot
yertle
bjvg xsb hxsn xsb qymm xsb rqat xsb pnetfn

# ✅ Sample Output:
# jane and puff and spot and yertle

# -------------------------------------------------------------
# 🔍 How It Works:
# The code maps each encrypted word to every possible dictionary word of the same length,
# checking if a consistent substitution exists. If yes, the substitution is extended;
# otherwise, the path is abandoned. This is done recursively until the full sentence is decrypted.

# -------------------------------------------------------------
# ⏱ Time Complexity:
# -------------------------------------------------------------
# Let:
#   - N be the number of words in the sentence.
#   - M be the number of words in the dictionary.
#   - L be the average length of a word.

# 🔸 Best-case: O(N * L)
#     - When the correct match is found on the first attempt at each step.
#     - No backtracking is needed.

# 🔸 Worst-case: O(M^N)
#     - When all combinations are explored due to no valid decryption path or many false leads.

# -------------------------------------------------------------
# 🧠 Space Complexity:
# -------------------------------------------------------------
# - O(M) to store dictionary.
# - O(L * 26) for substitution mappings (at most one char per alphabet letter).
# - O(N) call stack depth in recursion.

# 🔹 Overall: O(M + N + L)
"""

"""
Problem: Automated Judge Script
Given two sets of output lines (standard and obtained), determine if the outputs match exactly, have a presentation error, or are wrong answers. Presentation error means the numbers match but formatting (spaces, etc.) differs.

Input:
- Number of lines in standard output
- Standard output lines
- Number of lines in obtained output
- Obtained output lines

Output:
- For each run, print 'Accepted', 'Presentation Error', or 'Wrong Answer'.

Sample Input:
2
123 456
789 012
2
123 456
789 012

Sample Output:
Run #1: Accepted

Explanation:
If the obtained output matches the standard output exactly, it's 'Accepted'. If only the numbers match but formatting differs, it's 'Presentation Error'. Otherwise, it's 'Wrong Answer'.

Time Complexity: O(n*m), where n is the number of lines and m is the average line length.
Space Complexity: O(n), for storing the outputs.
"""

import re
Final_answer = []
std = []
obt = []

def Split(a):
    temp = ''
    try:
        int(a[0])
        start = 0
    except:
        start = 1
    if len(a) > 2:
        for i in range(start, len(a), 2):
            temp += a[i]
    else:
        temp = ''.join(a)
    return temp

def CheckPresentation(A, B, count):
    for i in range(count):
        a = re.split('(\d+)', A[i])
        b = re.split('(\d+)', B[i])
        a = Split(a[1:len(a)-1])
        b = Split(b[1:len(b)-1])
        if len(a) == len(b):
            for j in range(len(a)):
                if a[j] != b[j]:
                    return False
        else:
            return False
    return True

count = 1
while True:
    try:
        temp = int(input("Enter number of lines in input (<=0 to quit): "))
        if temp <= 0:
            break
        # Determine prompt based on input size
        if temp == 2:
            prompt = 'Enter output line: '
        else:
            prompt = 'Enter input line: '
        std = []
        obt = []
        print(f"Enter {temp} lines of STANDARD output:")
        for i in range(temp):
            line = input(f"{prompt}").rstrip('\n')
            std.append(line)
        temp1 = int(input(f"Enter number of lines in OBT output (should be {temp}): "))
        if temp != temp1:
            print("Mismatch in number of lines. Exiting.")
            break
        print(f"Enter {temp1} lines of OBT output:")
        for i in range(temp1):
            line = input(f"{prompt}").rstrip('\n')
            obt.append(line)
        if std == obt:
            Final_answer.append(f"Run #{count}: Accepted")
        else:
            if CheckPresentation(std, obt, temp):
                Final_answer.append(f"Run #{count}: Presentation Error")
            else:
                Final_answer.append(f"Run #{count}: Wrong Answer")
        count += 1
    except ValueError:
        # Handles invalid integer inputs and EOF (Ctrl+D / Ctrl+Z)
        break

print("\nResults:")
for res in Final_answer:
    print(res)

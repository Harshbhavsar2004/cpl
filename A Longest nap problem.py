# ---------------------------------------------------------------
# 📘 Problem: Longest Nap Between Appointments
# ---------------------------------------------------------------
# You are given daily appointments between 10:00 and 18:00.
# Each appointment has a start and end time (HH:MM format).
# The goal is to find the longest continuous free interval ("nap")
# between any two appointments, or before the first or after the last.

# 🕘 Office hours are from 10:00 (600 mins) to 18:00 (1080 mins)

# ---------------------------------------------------------------
# ✅ Sample Input:
# 4
# 10:00 12:00
# 13:00 15:00
# 15:30 16:00
# 16:30 17:00

# ✅ Sample Output:
# Day #1: the longest nap starts at 12:00 and will last for 60 minutes.

# 🔍 Explanation:
# Gaps:
# - 12:00 to 13:00 → 60 mins
# - 15:00 to 15:30 → 30 mins
# - 16:00 to 16:30 → 30 mins
# - 17:00 to 18:00 → 60 mins
# The earliest longest nap is from 12:00 to 13:00

# ---------------------------------------------------------------

# 🕘 Working hours in minutes
START_TIME = 10 * 60
END_TIME = 18 * 60

def to_minutes(hhmm: str) -> int:
    """Converts 'HH:MM' string to total minutes."""
    hh = int(hhmm[:2])
    mm = int(hhmm[3:])
    return hh * 60 + mm

def to_time_str(minutes: int) -> str:
    """Converts total minutes to 'HH:MM' formatted string."""
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

def find_longest_nap(apps):
    """Finds the longest nap interval between appointments."""
    # Convert time strings to minute intervals
    intervals = [(to_minutes(start), to_minutes(end)) for start, end in apps]
    intervals.sort()  # Sort by start time

    max_nap = -1
    max_start = START_TIME

    # Check for nap before first appointment
    if intervals[0][0] > START_TIME:
        nap = intervals[0][0] - START_TIME
        if nap > max_nap:
            max_nap = nap
            max_start = START_TIME

    # Check between appointments
    for i in range(1, len(intervals)):
        end_prev = intervals[i - 1][1]
        start_curr = intervals[i][0]
        if start_curr > end_prev:
            nap = start_curr - end_prev
            if nap > max_nap:
                max_nap = nap
                max_start = end_prev

    # Check for nap after last appointment
    if intervals[-1][1] < END_TIME:
        nap = END_TIME - intervals[-1][1]
        if nap > max_nap:
            max_nap = nap
            max_start = intervals[-1][1]

    return max_start, max_nap

def main():
    day = 0
    try:
        while True:
            line = input()
            if not line:
                break
            n = int(line.strip())
            day += 1
            apps = []
            for _ in range(n):
                raw = input()
                parts = raw.strip().split()
                apps.append((parts[0], parts[1]))  # (start, end)

            start_min, duration = find_longest_nap(apps)
            start_time = to_time_str(start_min)
            duration_hr = duration // 60
            duration_min = duration % 60

            print(f"Day #{day}: the longest nap starts at {start_time} and will last for ", end="")
            if duration_hr:
                print(f"{duration_hr} hours and {duration_min} minutes.")
            else:
                print(f"{duration_min} minutes.")
    except EOFError:
        pass  # graceful end for multiple test cases via stdin

if __name__ == "__main__":
    main()

# ---------------------------------------------------------------
# ⏱ Time Complexity:
# - to_minutes/to_time_str: O(1) each
# - Converting all appointments to minutes: O(n)
# - Sorting intervals: O(n log n)
# - Scanning for nap gaps: O(n)
# ✅ Total Time Complexity: O(n log n) per test case

# 🧠 Space Complexity:
# - intervals list: O(n)
# - constant variables and return values: O(1)
# ✅ Total Space Complexity: O(n)
# ---------------------------------------------------------------

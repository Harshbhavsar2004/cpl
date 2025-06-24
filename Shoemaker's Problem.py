# -----------------------------------------------
# Problem Explanation:
# We are given multiple jobs, each with:
# - T = time to complete
# - S = penalty/weight per unit time
# Goal: Schedule jobs to minimize the total weighted completion time.
# Strategy: Sort jobs by decreasing order of S/T ratio (Smith's Rule).
# If two jobs have the same S/T ratio, retain the original input order.

# -------------------------------------------------
# Sample Input:
# 1
# 4
# 3 4
# 1 1000
# 2 2
# 5 5

# Explanation:
# We have 1 test case with 4 jobs.
# Each line has two values: T (processing time), S (weight).
# Convert to (S, T, pos): (4, 3, 1), (1000, 1, 2), (2, 2, 3), (5, 5, 4)
# Calculate S/T: 1.33, 1000.0, 1.0, 1.0
# Sorted by descending S/T gives order: Job 2, Job 1, Job 3, Job 4

# Sample Output:
# Optimal job order:
# 2 1 3 4

# --------------------------------------------------
from typing import List

# Define the job structure
class Job:
    def __init__(self, S: int, T: int, pos: int):
        self.S = S  # weight
        self.T = T  # time
        self.pos = pos  # original position

# Define the comparator logic
def compare_jobs(job: Job) -> tuple:
    ratio = job.S / job.T  # Smith's rule: maximize S/T
    return (-ratio, job.pos)  # Sort descending by S/T; if tie, preserve input order

def main():
    N = int(input("Enter the number of test cases: "))

    for test_case in range(N):
        n = int(input(f"\nEnter the number of jobs for test case {test_case + 1}: "))
        jobs: List[Job] = []

        print("Enter the processing time (T) and weight (S) for each job:")
        for i in range(n):
            T, S = map(int, input(f"Job {i + 1}: ").split())
            jobs.append(Job(S, T, i + 1))  # Store (S, T, position)

        # Sort using the custom key
        jobs.sort(key=compare_jobs)

        # Print the order of job positions
        print("Optimal job order:")
        print(' '.join(str(job.pos) for job in jobs))

        if test_case != N - 1:
            print()

if __name__ == "__main__":
    main()

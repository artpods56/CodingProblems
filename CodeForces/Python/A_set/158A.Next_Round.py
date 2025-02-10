# cf_158A:10_02_2025
# https://codeforces.com/contest/158/problem/A

import sys
from io import StringIO

input_data = """4 2
0 0 0 0
"""

sys.stdin = StringIO(input_data)

# -- solution --

n, k = map(int, input().split())

count = 0
scores = list(map(int, input().split()))

for num in scores:
    if num >= scores[k - 1] and num > 0:
        count += 1

print(count)

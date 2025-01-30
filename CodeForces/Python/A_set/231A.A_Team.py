
#cf_A71:30_01_2025

import sys
from io import StringIO

input_data = """3
1 1 0
1 1 1
1 0 0
"""

sys.stdin = StringIO(input_data)

# -- solution --

n = int(input())

total_count = 0
for _ in range(n):
    line = list(map(int,input().split()))
    total_count += 1 if line.count(1) >= 2 else 0
print(total_count)


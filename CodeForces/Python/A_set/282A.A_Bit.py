#cf_282A:30_01_2025

import sys
import io

input_data = """1
++X
"""

sys.stdin = io.StringIO(input_data)

# -- solution --
x = 0
n = int(input())

for _ in range(n):
    match input()[1]:
        case "+":
            x += 1
        case "-":
            x -= 1

print(x)


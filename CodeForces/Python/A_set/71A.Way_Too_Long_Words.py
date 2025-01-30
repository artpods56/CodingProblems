#cf_A71:30_01_2025

import sys
from io import StringIO

input_data = """4
word
localization
internationalization
pneumonoultramicroscopicsilicovolcanoconiosis
"""

sys.stdin = StringIO(input_data)

# -- solution --

n = int(input())
for _ in range(n):
    line = input()
    line_len = len(line)
    if line_len > 10:
        print("".join([line[0],str(line_len-2),line[-1]]))
    else:
        print(line)


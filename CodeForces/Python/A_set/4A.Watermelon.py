#cf_A4:26_01_2025

input: int = int(input())

def can_divide(input: int):
    for i in range(2,input,2):
        if (input - i) % 2 == 0:
            return True
    return False


if can_divide(input):
    print("YES")
else:
    print("NO")


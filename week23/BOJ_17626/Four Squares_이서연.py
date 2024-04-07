import sys

input = sys.stdin.readline

n = int(input().strip())

is_square = [False] * (n + 1)

i = 1

while i * i <= n:
    is_square[i * i] = True
    i += 1

result = 4

for i in range(int(n ** 0.5), 0, -1):
    if is_square[n]:
        result = 1
        break

    if is_square[n - (i ** 2)]:
        result = 2
        break
    else:
        for j in range(int((n - (i ** 2)) ** 0.5), 0, -1):
            if is_square[n - (i ** 2) - (j ** 2)]:
                result = 3

print(result)
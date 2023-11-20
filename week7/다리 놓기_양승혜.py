# nCr
def factorial(number):
    start = 1
    for num in range(1, number + 1):
        start *= num
    return start

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(m - n) * factorial(n)))

# dp
bridge = [[0] * 30 for _ in range(30)]

for i in range(30):
    for j in range(30):
        if i == 1:
            bridge[i][j] = j
        elif i == j:
            bridge[i][j] = 1
        elif i < j:
            bridge[i][j] = bridge[i - 1][j - 1] + bridge[i][j - 1]

for _ in range(int(input())):
    n, m = map(int, input().split())
    print(bridge[n][m])

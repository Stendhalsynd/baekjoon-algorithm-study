n = int(input())
m = int(input())

room = [False] * (n + 1)

for i in range(0, m, 1):
    x, y = map(int, input().split())
    room[x] = True  
    for j in range(x + 1, y, 1):
        room[j] = True

count = 0

for i in range(1, n+1, 1):
    if room[i] == False:
        count = count + 1

print(count)
king, stone, N = map(str, input().split())

row = ["A", "B", "C", "D", "E", "F", "G", "H"]
move = {"R": [0, 1], "L": [0, -1], "B": [1, 0], "T": [-1, 0], 
        "RT": [-1, 1], "LT": [-1, -1], "RB": [1, 1], "LB": [1, -1]}

k1, k2 = 8 - int(king[1]), row.index(king[0])
s1, s2 = 8 - int(stone[1]), row.index(stone[0])

for _ in range(int(N)):
    a, b = move[input()]
    if 0 <= k1 + a < 8 and 0 <= k2 + b < 8:
        k1 += a
        k2 += b
        if k1 == s1 and k2 == s2:
            s1 += a
            s2 += b
    if s1 < 0 or s1 >= 8 or s2 < 0 or s2 >= 8:
        k1 -= a
        k2 -= b
        s1 -= a
        s2 -= b

print(f"{row[k2]}{8 - k1}") # 7 0 6 0
print(f"{row[s2]}{8 - s1}")

import sys

input = sys.stdin.readline

king, rock, n = map(str, input().split())
n = int(n)


alphabet = ["A", "B", "C", "D", "E", "F", "G", "H"]
movings = {"R": (1, 0), "L": (-1, 0), "B": (0, -1), "T": (0, 1), "RT": (1, 1), "LT": (-1, 1), "RB": (1, -1), "LB": (-1, -1)}

k1, k2 = (alphabet.index(king[0]), int(king[1]))
r1, r2 = (alphabet.index(rock[0]), int(rock[1]))
    
for i in range(n):
    move = input().strip()
    
    if -1 < k1 + movings[move][0] < 8 and 0 < k2 + movings[move][1] < 9:
        k1 += movings[move][0]
        k2 += movings[move][1]
    
    if k1 == r1 and k2 == r2:
        if -1 < r1 + movings[move][0] < 8 and 0 < r2 + movings[move][1] < 9:
            r1 += movings[move][0]
            r2 += movings[move][1]
        else:
            k1 -= movings[move][0]
            k2 -= movings[move][1]
    

print(alphabet[k1] + str(k2))
print(alphabet[r1] + str(r2))
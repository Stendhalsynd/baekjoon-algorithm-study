# 구현, 시뮬레이션
import sys
input = sys.stdin.readline

Sl, Sr = input().rstrip().split()
str = input().rstrip()

keyboard = {'q': [0, 0], 'w': [0, 1], 'e': [0, 2], 'r': [0, 3], 't': [0, 4], 'y': [0, 5], 'u': [0, 6], 'i': [0, 7], 'o': [0, 8], 'p': [0, 9],
            'a': [1, 0], 's': [1, 1], 'd': [1, 2], 'f': [1, 3], 'g': [1, 4], 'h': [1, 5], 'j': [1, 6], 'k': [1, 7], 'l': [1, 8],
            'z': [2, 0], 'x': [2, 1], 'c': [2, 2], 'v': [2, 3], 'b': [2, 4], 'n': [2, 5], 'm': [2, 6]}

left = 'qwertasdfgzxcv'
total = 0

for s in str:

  leftY, leftX = keyboard[Sl]
  rightY, rightX = keyboard[Sr]

  if s in left:
    total += abs(leftY - keyboard[s][0]) + abs(leftX - keyboard[s][1]) + 1
    Sl = s
  else:
    total += abs(rightY - keyboard[s][0]) + abs(rightX - keyboard[s][1]) + 1
    Sr = s

print(total)
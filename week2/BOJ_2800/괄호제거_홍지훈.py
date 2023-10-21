import sys
from itertools import combinations

stack = list([ str for str in sys.stdin.readline().rstrip()])

bracketStack, pair = [], []
answer = set()

for idx, val in enumerate(stack):
  if val == '(':
    bracketStack.append(idx)
  elif val == ')':
    start, end = bracketStack.pop(), idx
    pair.append((start, end))

cases = []

for i in range(len(pair)):
  cases.append(list(combinations(pair, i + 1)))

for detail in cases:
  for case in detail:
    data = stack[:]
    for front, back in case:
      data[front] = ''
      data[back] = ''
      answer.add(''.join(data))

for str in sorted(list(answer)):
  print(str)
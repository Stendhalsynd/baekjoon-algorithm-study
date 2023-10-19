import sys

stack = list([ str for str in sys.stdin.readline().rstrip()])

numRightBracket = 1
previous = stack.pop()
result = 0

for i in range(1, len(stack) + 1):
  last = stack.pop()
  if last == ')': 
    numRightBracket += 1
    previous = ')'
  elif last == '(' and previous == ')':
    numRightBracket -= 1
    result += numRightBracket
    previous = '('
  elif last == '(' and previous == '(':
    result += 1
    numRightBracket -= 1
    previous = '('

print(result)

  
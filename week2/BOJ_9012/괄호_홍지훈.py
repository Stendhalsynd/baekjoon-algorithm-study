import sys

N = int(sys.stdin.readline().rstrip())
result = []

for num in range(N):
  input = sys.stdin.readline().rstrip()
  stack = []
  isValid = True

  for str in input:
    if str == "(":
      stack.append(str)
    else:
      if stack:
        stack.pop()
      else:
        isValid = False
        break

  if not stack and isValid:
    result.append("YES")
  else:
    result.append("NO")

for res in result:
  print(res)
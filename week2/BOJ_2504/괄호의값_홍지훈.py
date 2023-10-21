# 구현, 자료구조, 스택

import sys

inputStr = sys.stdin.readline().rstrip()
dic = {'(':')','[':']'}
stack = []
temp = 1
sum = 0
check = True

for char in inputStr:
  
  # 여는 괄호라면 스택에 추가
  if char in dic: 
    check = True
    stack.append(char) 
    if char == '(': temp *= 2 # ( 는 항상 * 2
    else: temp *= 3 # [ 는 항상 * 3

  # 닫는 괄호일 경우
  else:
    if not stack:
      sum = 0
      break
    last = stack.pop()
    # 닫는 쌍이 맞는 경우
    if dic[last] == char:
      if check:  # 바로 이전까지 여는 괄호였을 경우에만 sum 에 더한다.
        sum += temp
        check = False 

      if char == ')': # ) 는 그때까지의 temp 를 sum 에 더하고 temp 를 2 로 나눈다.
        temp //= 2 
      elif char == ']': # ] 는 그때까지의 temp 를 sum 에 더하고 temp 를 3 으로 나눈다.
        temp //= 3

    # 닫는 괄호만 있었을 경우, 여는 괄호와 닫는 괄호 쌍이 맞지 않는 경우
    elif len(stack) == 0 or dic[last] != char:
      sum = 0
      break

if stack:
  print(0)
else:
  print(sum)
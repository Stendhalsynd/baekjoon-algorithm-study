import sys
input = sys.stdin.readline
from sys import maxsize

N = int(input().rstrip())

def count_odd(num):
  result = 0
  for char in str(num):
    if int(char) % 2 == 1:
      result += 1
  return result

def add_each_num(num):
  return num // 10 + num % 10

response = [maxsize, -maxsize]

def find_min_and_max(target, counter):
  string_target = str(target)
  if len(string_target) == 1:
    response[0] = min(counter, response[0])
    response[1] = max(counter, response[1])
    return
  elif len(string_target) == 2:
    next = add_each_num(target)
    return find_min_and_max(next, counter + count_odd(next))
  else:
    for i in range(1, len(string_target)):
      for j in range(i + 1, len(string_target)):
        segment1 = string_target[:i]
        segment2 = string_target[i:j]
        segment3 = string_target[j:]
        next = int(segment1) + int(segment2) + int(segment3)
        find_min_and_max(next, counter + count_odd(next))

find_min_and_max(N, count_odd(N))

print(*response)


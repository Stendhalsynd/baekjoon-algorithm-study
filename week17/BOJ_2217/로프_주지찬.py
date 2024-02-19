
import sys
sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
arr = []

for i in range(n):
  arr.append(int(sys.stdin.readline()))

arr.sort()

length = len(arr)


result = 0

for i,j in enumerate(arr):
  result = max(result,j*(n-i))

print(result)




# for i,j in enumerate(arr):
#   temp = 0
#   for k,l in enumerate(arr):
#     if k >= i:
#       temp += min(j,l)
  
#   result = max(result, temp)

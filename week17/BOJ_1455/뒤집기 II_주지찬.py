import sys
sys.stdin = open('input.txt')
n, m = map(int, (sys.stdin.readline().split(' ')))

# 동전 뒤집는 함수
def flip(arr, a, b):
  temp = arr
  for i in range(0, a+1):
    for j in range(0, b+1):
      if temp[i][j] == 0:
        temp[i][j] = 1
      else:
        temp[i][j] = 0
  print(temp)
  return temp


# 동전판 만들기
arr = []

cnt = 0
for i in range(n):
  temp = list(map(int, (list(sys.stdin.readline().replace('\n','')))))
  arr.append(temp)
# 동전판 순회하기
for i in range(n-1, -1, -1):
  for j in range(m-1, -1, -1):
    if arr[i][j]:
      cnt += 1
      arr = flip(arr, i, j)

print(cnt)

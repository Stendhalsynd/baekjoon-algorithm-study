import sys
input = sys.stdin.readline

N = int(input()) # N: 사람의 수
info = list(map(int, input().rstrip().split())) # 키가 1부터 자신보다 키가 큰 사람이 왼쪽에 몇명 있었는지
result = [0] * N


'''
키가 작은 순서대로 자신이 몇번째인지 알 수 있는 것 같다.
1 -> 2 : 1의 인덱스가 2

두번째 이후부터 첫번째를 제외하고 생각해보자.

2 -> 1 : 2의 인덱스가 1

3 -> 1 : 3의 인덱스가 1 ? 1이 이미 있다 -> 2 ? 2가 이미 있다 -> 3

4 -> 0 : 4의 인덱스가 0

N: 10
info = [5, 3, 7, 1, 4, 2, 1, 0, 0, 0]
result :  [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
result :  [0, 0, 0, 2, 0, 1, 0, 0, 0, 0]
result :  [0, 0, 0, 2, 0, 1, 0, 0, 0, 3]
result :  [0, 4, 0, 2, 0, 1, 0, 0, 0, 3]
result :  [0, 4, 0, 2, 0, 1, 0, 5, 0, 3]
result :  [0, 4, 0, 2, 6, 1, 0, 5, 0, 3]
result :  [0, 4, 7, 2, 6, 1, 0, 5, 0, 3]
result :  [8, 4, 7, 2, 6, 1, 0, 5, 0, 3]
result :  [8, 4, 7, 2, 6, 1, 9, 5, 0, 3]
result :  [8, 4, 7, 2, 6, 1, 9, 5, 10, 3]
'''

for idx, val in enumerate(info): 
  if result[val] == 0:                 # 만약 result 의 val 인덱스가 0이라면
    empty = result[:val].count(0)      # empty : result 의 val 인덱스 전까지 비어있는 칸의 수
    if empty == val:                   # empty 와 val 이 같다는 것은 그때까지 앞에 채워진 적이 없다는 것을 의미합니다.
      result[val] = idx + 1
    elif empty < val:                  # empty 보다 val 이 크다는 것은 앞에 채워진 값이 존재한다는 것을 의미합니다.
      count = val - empty              # 최소한 val - empty 만큼은 인덱스를 더해야 idx + 1 (타겟) 보다 큰 사람들이 줄을 설 수 있습니다.
      curr = val
      while count > 0:                 # count 는 자신보다 큰 사람중 앞에 부족한 빈자리를 의미합니다.
        if result[curr] == 0:          # 만약 현재 위치 curr 이 비어있다면 count 를 1 감소시키고 현재 인덱스 curr 를 1 증가시킵니다.
          count -= 1
          curr += 1
        else:                          # 만약 현재 위치 curr 가 채워져있다면 현재 인덱스 curr 만 1 증가시킵니다.
          curr += 1
      while result[curr] != 0:         # 도중에 현재 위치 curr 이 채워져있다면 비어있는 칸이 나올때까지 현재 인덱스 curr 를 증가시킵니다.
        curr += 1

      result[curr] = idx + 1           # 그렇게 최종 위치 curr 을 업데이트시키고 사람 idx + 1 을 배치합니다.

  else:                                # 만약 result 의 val 인덱스가 처음부터 채워져 있다면
    count = val
    i = 0
    while result[i] != 0 or count > 0: # 앞에서부터 result 가 비어있는 만큼 인덱스 i 를 증가시키고 해당 위치에 사람 idx + 1 을 배치합니다.
      if result[i] == 0:
        count -= 1
      i += 1


    result[i] = idx + 1

for v in result:
  print(v, end=' ')
print()
import sys
from collections import deque

# 입력 처리
Num = int(sys.stdin.readline().rstrip())  # 전체 테스트 케이스 수
result = []

for i in range(Num):  # 테스트 케이스만큼 입력을 받는다.
  N, M = map(int, sys.stdin.readline().rstrip().split()) # 문서의 개수, 몇 번째로 인쇄되어있는지 궁금한 문서가 Queue 상에 몇번째에 놓여 있는지
  importance = list(map(int, sys.stdin.readline().rstrip().split()))  # N 개 문서의 중요도, 1 ~ 9, 중요도가 같을 수도 있다.
  deq = deque([(val, idx) for idx, val in enumerate(importance)])  

  count = 0
  while deq:
    max_val = max(deq, key=lambda x: x[0])  # 큐에서 중요도가 가장 높은 값
    doc = deq.popleft()
    
    if doc[0] < max_val[0]: # 중요도가 가장 높은 문서가 아니면 큐의 맨 뒤로 append
      deq.append(doc)  
    else:
      count += 1  # 중요도가 가장 높은 문서
      if doc[1] == M:  # 찾고자 하는 문서
        result.append(count)

for count in result:
  print(count)

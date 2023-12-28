"""
Input: 
- N(민혁이가 영수에게 질문한 횟수)
- 민혁이가 질문한 3자리 수, 영수가 답한 스트라이크 개수, 볼의 개수
Output: 영수가 생각하고 있을 가능성이 있는 답의 총 개수

스트라이크: 민혁이가 말한 3자리 수에 있는 숫자들 중 하나가 영수의 3자리 수의 동일한 자리에 위치할 때
볼: 숫자가 영수의 세자리 수에 있긴 하나 다른 자리에 위치할 때

전체 시간복잡도 O(N * 9P3)
"""
import sys
from itertools import permutations

# sys.stdin.readline().rstrip() -> 표준 입력에서 한 줄을 읽어오고 개행 문자를 제거한 문자열을 얻을 수 있다.
# sys.stdin: standard input stream
# readline(): 한 줄을 읽어논다.
# rstrip(): 문자열의 끝의 공백 문자(보통은 개행 문자 '\n'를 제거하는 역할

N = int(sys.stdin.readline().rstrip())

numbers = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3)) # 시간복잡도: 입력의 크기가 고정되어 있으므로, 상수 시간에 수행된다고 할 수 있다. -> O(1)

for _ in range(N): # 시간복잡도: O(N)
  question_number, strike, ball = map(int, sys.stdin.readline().split())
  question_number = list(str(question_number))
  removed = 0

  for i in range(len(numbers)): # 시간복잡도: 최악의 경우, O(9P3)
    strike_count = 0
    ball_count = 0

    # 요소가 제거된만큼 인덱스 조정
    i -= removed

    # 스트라이크, 볼 개수 확인
    for j in range(3):
      if numbers[i][j] == question_number[j]:
        strike_count += 1
      elif question_number[j] in numbers[i]:
        ball_count += 1
    
    # 스트라이크 or 볼의 개수가 맞지 않으면 리스트에서 제거
    if strike_count != strike or ball_count != ball:
      numbers.remove(numbers[i])
      removed += 1

print(len(numbers))
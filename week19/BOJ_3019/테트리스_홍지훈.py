import sys
input = sys.stdin.readline

# 1 <= C <= 100, 1 <= P <= 7
C, P = map(int, input().rstrip().split()) # C: 열 P: 떨어뜨리는 블록의 번호
heights = list(map(int, input().rstrip().split()))
types = [0 for _ in range(13)]
types[0] = C
'''
각 블럭별로 정면, 90, 180, 270 4가지 종류의 타입을 갖고
1 ~ C 까지 움직일 수 있다.

각 블럭 타입별로 올 수 있는 유형을 정리해야 한다.
1번 블럭)
모든칸 / 4칸 연속 같은 높이

2번 블럭)
2칸 연속 같은 높이

3번 블럭)
3칸 오른쪽 칸이 한칸 높게 / 2칸 왼쪽 칸이 한칸 높게

4번 블럭)
3칸 왼쪽 칸이 한칸 높게 / 2칸 오른쪽 칸이 한칸 높게

5번 블럭)
3칸 연속 같은 높이 / 2칸 오른쪽 칸이 한칸 높게 / 3칸 양 옆이 한칸 높게 / 2칸 왼쪽 칸이 한칸 높게

6번 블럭)
3칸 연속 같은 높이 / 2칸 연속 같은 높이 / 3칸 왼쪽 칸이 한칸 낮게 / 2칸 왼쪽 칸이 두칸 높게

7번 블럭)
3칸 연속 같은 높이 / 2칸 연속 같은 높이 / 2칸 오른쪽 칸이 두칸 높게 / 3칸 오른쪽 칸이 한칸 낮게

=> 유형을 나눠보자 types = [a0, a1, a2, a3, b0, b1, b2, b3, b4, c0, c1]
0 모든칸 C
1 4칸 연속 같은 높이
2 3칸 연속 같은 높이
3 2칸 연속 같은 높이

4 3칸 오른쪽 한칸 높
5 3칸 왼쪽 한칸 높
6 3칸 오른쪽 한칸 낮
7 3칸 왼쪽 한칸 낮
8 3칸 양옆 한칸 높

9 2칸 왼쪽 한칸 높
10 2칸 오른쪽 한칸 높

11 2칸 왼쪽 두칸 높
12 2칸 오른쪽 칸 두칸 높
'''

for i in range(C - 1):
  # 4칸 연속 같은 높이인가
  if C >= 4 and i + 3 <= C - 1 and max(heights[i: i + 4]) == min(heights[i: i + 4]): types[1] += 1
  # 3칸 연속 같은 높이인가
  if C >= 3 and i + 2 <= C - 1 and max(heights[i: i + 3]) == min(heights[i: i + 3]): types[2] += 1
  # 2칸 연속 같은 높이인가
  if C >= 2 and i + 1 <= C - 1 and max(heights[i: i + 2]) == min(heights[i: i + 2]): types[3] += 1
  # 3칸중 오른쪽 칸이 한칸 높은가
  if C >= 3 and i + 2 <= C - 1 and heights[i] == heights[i + 1] == heights[i + 2] - 1: types[4] += 1
  # 3칸중 왼쪽 칸이 한칸 높은가
  if C >= 3 and i + 2 <= C - 1 and heights[i] - 1 == heights[i + 1] == heights[i + 2]: types[5] += 1
  # 3칸중 오른쪽 칸이 한칸 낮은가
  if C >= 3 and i + 2 <= C - 1 and heights[i] == heights[i + 1] == heights[i + 2] + 1: types[6] += 1
  # 3칸중 왼쪽 칸이 한칸 낮은가
  if C >= 3 and i + 2 <= C - 1 and heights[i] + 1 == heights[i + 1] == heights[i + 2]: types[7] += 1
  # 3칸중 양옆이 한칸 높은가
  if C >= 3 and i + 2 <= C - 1 and heights[i] - 1 == heights[i + 1] == heights[i + 2] - 1: types[8] += 1
  # 2칸중 왼쪽이 한칸 높은가
  if C >= 2 and i + 1 <= C - 1 and heights[i] - 1 == heights[i + 1]: types[9] += 1
  # 2칸중 오른쪽이 한칸 높은가
  if C >= 2 and i + 1 <= C - 1 and heights[i] == heights[i + 1] - 1: types[10] += 1
  # 2칸중 왼쪽이 두칸 높은가
  if C >= 2 and i + 1 <= C - 1 and heights[i] - 2 == heights[i + 1]: types[11] += 1
  # 2칸중 오른쪽이 두칸 높은가
  if C >= 2 and i + 1 <= C - 1 and heights[i] == heights[i + 1] - 2: types[12] += 1

def game(block):
  global types
  if block == 1:
    return types[0] + types[1]
  elif block == 2:
    return types[3]
  elif block == 3:
    return types[4] + types[9]
  elif block == 4:
    return types[5] + types[10]
  elif block == 5:
    return types[2] + types[10] + types[8] + types[9]
  elif block == 6:
    return types[2] + types[3] + types[7] + types[11]
  elif block == 7:
    return types[2] + types[3] + types[6] + types[12]
  
print(game(P))
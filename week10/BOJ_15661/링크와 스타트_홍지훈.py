# import sys
# input = sys.stdin.readline
# from itertools import permutations
# MAX = 1e9
# min_diff = MAX
# sys.setrecursionlimit(10**7)

# N = int(input().rstrip()) # N : 모인 사람의 수, 4 <= N <= 20
# members = [i for i in range(1, N + 1)]

# graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# for i in range(1, N + 1):
#   S = list(map(int, input().rstrip().split())) # Sii == 0, 1 <= Sij <= 100
#   for j in range(1, N + 1):
#     graph[i][j] = S[j - 1]

# def back(k):
#   global min_diff
#   if k == len(total_case):
#     print(min_diff)
#     return
  
#   teams = total_case[k]
#   team1, team2 = teams
#   result, val = is_valid(team1, team2)
#   if result:
#     min_diff = val

#   back(k + 1)

# def is_valid(team1, team2): # 유망 조건
#   if len(team1) == 0 or len(team1) == N:
#     return False, 0
#   team1_score = 0
#   team2_score = 0

#   for members in list(permutations(team1, 2)):
#     i, j = members
#     team1_score += graph[i][j]
#   for members in list(permutations(team2, 2)):
#     i, j = members
#     team2_score += graph[i][j]

#   if abs(team1_score - team2_score) < min_diff:
#     return True, abs(team1_score - team2_score)
#   return False, 0

# def all_splits(arr):
#     all_cases = []

#     # 부분집합을 생성하기 위한 이진 표현을 이용
#     for i in range(2**(len(arr)-1)):
#         subset1 = [arr[j] for j in range(len(arr)) if (i & (1 << j)) > 0]
#         subset2 = [arr[j] for j in range(len(arr)) if (i & (1 << j)) == 0]

#         # 두 부분이 모두 비어있지 않은 경우에만 추가
#         if subset1 and subset2:
#             all_cases.append([subset1, subset2])

#     return all_cases

# total_case = all_splits(members)

# back(0)

from itertools import combinations
import sys

input = sys.stdin.readline


N = int(input())
score_list = [[*map(int, input().split())] for _ in range(N)]
answer = float("inf")
row = [sum(s) for s in score_list]
col = [sum(s) for s in zip(*score_list)]
arr = [sum(x) for x in zip(row, col)]
total = sum(arr) // 2

for i in range(1, N // 2 + 1):
    for c in combinations(arr, i):
        answer = min(answer, abs(total - sum(c)))

print(answer)

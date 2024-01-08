"""
Input: 문자열 2개
Output: 두 문자열의 LCS의 길이
전체 시간복잡도: O(nm)
공간복잡도: (n + 1) * (m + 1) 크기의 행렬을 사용 -> O(nm)

임의의 두 문자열에서 각각의 sub sequence가 같을 때, 가장 긴 길이를 구하는 문제

ACAYKP
CAPCAK
첫번째 문자열의 sub sequence를 s1, 두번째 문자열의 sub sequence를 s2라고 했을 때 문자를 하나씩 늘려가면서 비교하면

s1: A
s2: C
LCS = 0

s1: A
s2: CA
LCS = 1

s1: A
s2: CAP
LCS = 1

s1: A
s2: CAPC
LCS = 1

...

s1: AC
s2: C
LCS = 1

s1: AC
s2: CA
LCS = 1

...

계속 반복

s1과 s2에 가장 최근에 추가된 글자가 서로 같을 때, matrix[i][j] = matrix[i-1][j-1]+1 길이는 (두 글자가 추가되기 전 가장 큰 길이 + 1)이 된다.
s1과 s2에 가장 최근에 추가된 글자가 서로 다르다면, matrix[i][j] = max(matrix[i][j-1], matrix[i-1][j]) 기존에 주어진 문자열로 만들 수 있던 최대 길이를 갖게 된다.

matrix[3][6]
s1: ACA
s2: CAPCA
추가된 문자가 A로 일치하기 때문에 이 문자를 LCS에 포함시킨다고 하면 AC와 CAPC일 때의 최대 길이 + 1을 하면 된다. -> matrix[3][6] = matrix[2][5] + 1

matrix[7][7]
s1: ACAYKP
s2: CAPCAK
추가된 문자가 서로 다르기 때문에 추가된 문자를 LCS에 포함시킬 수 없는 상황이다.
ACAYK와 CAPCAK일 때의 LCS 길이와 ACAYKP와 CAPCA일 때의 LCS 길이 중 더 큰 값이 현재 만들 수 있는 가장 큰 LCS 길이 값이다. -> matrix[7][7] = max(matrix[6][7], matrix[7][6])
"""
import sys

S1 = sys.stdin.readline().strip().upper()
S2 = sys.stdin.readline().strip().upper()
len1 = len(S1)
len2 = len(S2)
matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)] # (n + 1) * (m + 1) 크기의 행렬 초기화 -> 시간복잡도: O(1)

for i in range(1, len1 + 1): # 중첩된 루프의 반복 횟수 (n + 1) * (m + 1) -> 시간복잡도: O(nm)
    for j in range(1, len2 + 1):
        if S1[i - 1] == S2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
        else:
            matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

print(matrix[-1][-1])
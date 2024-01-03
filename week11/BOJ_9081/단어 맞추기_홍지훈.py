import sys
input = sys.stdin.readline

def next_permutation(s):
    i = len(s) - 1
    while i > 0 and s[i - 1] >= s[i]: # i : 리스트를 뒤에서부터 탐색하며 현재 원소가 바로 뒤의 원소보다 작은 첫 번째 인덱스
        i -= 1

    if i == 0:
        return s

    j = len(s) - 1 # j : i 이전중 i - 1 보다 작거나 같은 첫 번째 원소
    while s[j] <= s[i - 1]:
        j -= 1

    s[i - 1], s[j] = s[j], s[i - 1] # j 와 i - 1 을 교환
    s[i:] = reversed(s[i:]) # i 이후를 뒤집어서 순열 증가 => 가장 작은 다음 순열 생성
    return s

T = int(input().rstrip())

for _ in range(T):
    word = list(input().rstrip())
    result = next_permutation(word)
    print(''.join(result))
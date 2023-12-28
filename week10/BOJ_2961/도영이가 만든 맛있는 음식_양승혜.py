from itertools import combinations

N = int(input())
bitters, sweets = [], []
results = []

for _ in range(N):
    b, s = map(int, input().split())
    bitters.append(b)
    sweets.append(s)

for i in range(1, N + 1):
    cases = list(combinations(list(range(N)), i))  # 가능한 케이스들을 중복이 없고, 순서를 고려하지 않는 combinations로 추출
    for case in cases:
        bitter, sweet = 1, 0
        for i in range(len(case)):
            bitter *= bitters[case[i]]  
            sweet += sweets[case[i]]
        results.append(abs(bitter - sweet))  # 절대값을 저장 - 마이너스가 나올수도 있으므로
print(min(results))  # 가장 작은 값을 도출

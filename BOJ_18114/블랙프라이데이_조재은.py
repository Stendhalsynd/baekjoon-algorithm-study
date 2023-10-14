import sys
# 서로 다른 n개 에서 r개를 선택할 때, 순서를 고려하지 않고 중복 없이 뽑을 경우의 수를 만들어 주는 모듈
# 형식 : combinations(객체, r). 반복 가능한 객체 (리스트/튜플/문자열)안에서 r개를 선택
# 예 : combination(ABCD, 2) => AB, AC, AD, BC, BD, CD *순서를 고려 안 하기 때문에, AB=BA 같다고 판단함
# 같은 물건을 중복 선택하는 것은 불가능하다고 적혀있기 때문에 사용 적합!
# 2
from itertools import combinations

# 함수 정의
# 입력받은 무게의 list와 제시 무게c를 파라메터로 받음
def find_list(weights_list, c):
    for r in range(1, min(n, 3) + 1): # 1개부터 최대 3개 까지 물건을 선택하는 경우를 모두 고려
        for combo in combinations(weights_list, r): # 조합을 이용해서 c 값 찾기
            print("combo:", combo)
            if sum(combo) == c: # 조합된 숫자들의 집계한 값이 c와 맞는지 확인
                return True

    return False

# 입력값 받기
n, c = map(int, input().split()) # 첫 번째 줄에 물건의 개수 N, 제시하는 무게 C
weights = list(map(int, input().split())) # N개의 물건 각각의 무게 w

if find_list(weights, c):
    print("1")
else:
    print("0")
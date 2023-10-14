from itertools import combinations
# 주석 수정
def find_list(acidic, alkaline):
    min_mixture = float('inf') # 더한값 리스트, 양의 무한대
    result = (0, 0) # 두 용액 저장값

    print(acidic, alkaline)

    for acid in acidic:
        for base in alkaline:
            mixture = acid + base
            if abs(mixture) < min_mixture:
                min_mixture = abs(mixture)
                result = (acid, base)

    return result

# 입력값 받기
n = int(input()) # 첫째 줄에는 전체 용액의 수
values = list(map(int, input().split())) # 용액의 특성값, 산성, 알칼리
# 산성 용액과 알칼리성 용액 분리
acidic_values = [x for x in values if x > 0]
alkaline_values = [x for x in values if x <= 0]

# 두 용액 찾기
result = find_list(acidic_values, alkaline_values)
print(result[1], result[0])
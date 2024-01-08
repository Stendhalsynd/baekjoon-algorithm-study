from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course: 
        final = []
        for order in orders:
            for bundle in combinations(sorted(order), c):  # 메뉴의 개수만큼 메뉴의 조합을 구함. 단, 메뉴는 정렬되어있어야한다.
                final.append("".join(bundle)) # ('A', 'B') -> 'AB'
        
        frequency = Counter(final).most_common()  # 빈도가 가장 높은 메뉴부터 정렬되도록 most_common() 씀

        max = 0
        for freq in frequency:
            if freq[1] > max:
                max = freq[1]
        for freq in frequency:
            if freq[1] >= max and freq[1] > 1:  # max값보다 크거나 같고 1명 이상의 고객이 썼을 경우
                answer.append(freq[0])
            else:
                break
    return sorted(answer)  # 정렬해서 answer 반환

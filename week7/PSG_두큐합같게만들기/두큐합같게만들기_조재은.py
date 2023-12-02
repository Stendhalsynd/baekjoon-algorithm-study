'''
1. queue1과 queue2의 길이는 같다
2. queue1과 queue2의 합을 같게 만들어야 한다.
----------------------------------------
- 최적의 해를 찾아가는 방법
- 반복문 탈출 조건 찾기
=> 파라미터로 큐를 받는 큐 자료형을 사용하는 문제이며, 큐 자료형의 특성을 사용하기 위해 deque를 사용했다.
=> list의 pop(0)를 사용하면 시간 복잡도가 상승해서 시간 초과의 위험이 있어 popleft() 사용했다.
----------------------------------------
pop을 하면 배열의 첫 번째 요소가 추출되며, insert를 하면 배열의 끝에 원소가 추가된다.
원소의 합이 높은 쪽에서 낮은 쪽으로 원소를 옮기는 패턴을 찾을 수 있다.
'''

from collections import deque


def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    limit = (len(queue1)) * 4
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1 + tot2

    if total % 2 != 0:
        return -1

    while True:
        if tot1 > tot2:
            target = queue1.popleft()
            queue2.append(target)
            tot1 -= target
            tot2 += target
            answer += 1

        elif tot1 < tot2:
            target = queue2.popleft()
            queue1.append(target)
            tot1 += target
            tot2 -= target
            answer += 1

        else:
            break
        if answer == limit:
            answer = -1
            break
    return answer
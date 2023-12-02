from collections import deque

def solution(queue1, queue2):
    sum1, sum2 = sum(queue1), sum(queue2)
    q1, q2 = deque(queue1), deque(queue2)
    count, maxcount = 0, len(queue1) * 3
    
    while True:
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            count += 1
            sum1 -= num
            sum2 += num
        elif sum1 < sum2:
            num = q2.popleft()
            q1.append(num)
            count += 1
            sum1 += num
            sum2 -= num
        else:
            return count
        
        if count == maxcount:
            return -1

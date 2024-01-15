from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N + 1)) # deque([1, 2, 3, 4, 5, 6, 7])

answer = []

while queue:
    for _ in range(K - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())

print(str(answer).replace("[", "<").replace("]", ">"))

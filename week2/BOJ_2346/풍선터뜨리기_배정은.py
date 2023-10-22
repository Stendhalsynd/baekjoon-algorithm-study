from collections import deque
import sys

N = int(sys.stdin.readline())
papers = list(map(int, sys.stdin.readline().split()))

balloons = deque([[idx + 1, papers[idx]] for idx in range(len(papers))])

while len(balloons) > 0:
    front = balloons.popleft() # 제일 앞에 있는 풍선 뽑기
    print(front[0], end=" ")

    if len(balloons) > 0:
        if front[1] > 0:
            for _ in range(abs(front[1]) - 1):
                balloons.append(balloons.popleft())
        else:
            for _ in range(abs(front[1])):
                balloons.insert(0, balloons.pop())



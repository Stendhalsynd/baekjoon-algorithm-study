from collections import deque
def move(cur, idx):
    if idx==0: return cur*2
    elif idx==1: return cur+1
    else: return cur-1

def bfs(N, K):
    if N==K: return 0
    q = deque()
    q.append([N, 0])
    INF = int(21e8)
    visited = [INF]*400001

    while q:
        cur, sec = q.popleft()
        if cur==K: break
        for i in range(3):
            next = move(cur, i)
            next_sec = sec if i==0 else sec+1
            if next < -200000 or next > 200000: continue
            if visited[next]<next_sec: continue
            visited[next]=next_sec
            if i>0: q.append([next, next_sec])
            else: q.append([next, next_sec])
    return visited[K]

N, K = map(int, input().split())
print(bfs(N, K))


'''
1 1
-> 0

0 0
-> 0

1 100000
-> 5

0 100000
-> 6

3124 100000
-> 1

3126 100000
-> 1

50001 100000
-> 1

100000 1
-> 99999
'''
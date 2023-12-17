from heapq import *

# 입력
subin, brother = map(int, input().split())

# 다익스트라 사용
def dijsktra(start, aim):
    graph = [1e9] * 100001
    graph[start] = 0
    heap = []
    heappush(heap, (0, start))  # (걸린 시간 - 현재 : 0, 현재 위치 - 수빈의 위치) 추가

    while heap:
        time, curr = heappop(heap)

        for next in [(curr + 1, 1), (curr - 1, 1), (2 * curr, 0)]:  # 수빈이가 움직일 수 있는 경우를 모두 리스트에 튜플 형식으로 저장
            if 0 <= next[0] < 100001 and graph[next[0]] > time + next[1]:  # next[0] : 갈 수 있는 거리, next[1] : 걸리는 시간
                graph[next[0]] = time + next[1]   # 조건에 맞으면 걸리는 시간을 담은 graph의 값을 업데이트
                heappush(heap, (graph[next[0]], next[0]))   # (업데이트된 걸린 시간, 현재 위치) 저장
    print(graph[brother])   # 동생의 위치에 해당하는 최단시간을 프린트
    
dijsktra(subin, brother)   # 함수 호출

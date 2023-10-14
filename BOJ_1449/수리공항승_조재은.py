import sys

# 입력값 받기
n, l = map(int, input().split()) # 첫째 줄에 물이 새는 곳의 개수 N, 갖고 있는 테이프의 길이 L
m = list(map(int, input().split())) # 물이 새는 곳의 위치

# 위치 정렬
m.sort()

start = m[0] # 테이프를 붙일 시작점
tape = 1 # 필요한 테이프 갯수

print("m:", m)

for i in m[1:]:
    # (i+0.5)-(start-0.5)가 입력한 테이프 길이 보다 작으면 continue
    if (i + 0.5) + (start - 0.5) < l:
        # 기존 테이프 사용
        continue
    # 기존 테이프로 붙이지 못한다면
    else:
        start = i
        tape = tape + 1 # 테이프 새로 추가

print(tape)

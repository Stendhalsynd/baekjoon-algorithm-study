import sys

n = int(sys.stdin.readline()) #  입력 데이터의 수
data = list(enumerate((map(int, sys.stdin.readline().split())), start = 1)) #  (인덱스, 값) 인덱스 시작은 1부터
idx = 0 # 첫번째 idx 고정


while True: # data가 존재하는 동안
    if len(data) > 0:
        ret = data.pop(idx) # 추출값
        print(ret[0], end=' ') # 인덱스 출력
    else: break

    if ret[1] < 0 and data:                     # 다음 인덱스 위치가 음수면
        idx = (idx + ret[1]) % len(data)        # 왼쪽 으로
    elif ret[1] > 0 and data:                   # 다음 인덱스 위치가 양수면
        idx = (idx + (ret[1] - 1)) % len(data)  # 오른쪽 으로

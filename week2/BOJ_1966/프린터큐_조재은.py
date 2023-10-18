import sys

t = int(sys.stdin.readline()) # t개의 테스트 케이스

# q의 index m인 정수가 몇 번째에 출력 되는지

for i in range(t):
    n, m = map(int, input().split()) # n: 출력할 문서 길이 입력값, m : q의 m번째 index 입력값

    q = list(map(int, input().split())) # n개의 중요도 목록
    temp = [0 for _ in range(n)] # 0을 n개 만큼 넣어줌
    temp[m] = 1 # 입력한 index 번호의 리스트 값만 1을 넣어줌
    cnt = 0 # 최종적으로 출력될 아이

    while True:
        # q의 중요도가 큰 순서대로 처리되기 때문에, q[0] 값이 q 리스트의 max 와 같은지 비교
        if q[0] == max(q):
            cnt += 1
            # 중요도가 같은 경우
            # 찾으려는 q의 인덱스 m번째의 요소가 1이 아니면 q[0], temp[0] pop 시켜줌
            if temp[0] != 1:
                q.pop(0)
                temp.pop(0)
            else:
                print(cnt)
                break
        # max 값이 0번째가 아니라면 q[0] 번째는 가장 뒷쪽으로 append, temp도 마찬가지
        else:
            q.append(q.pop(0))
            temp.append(temp.pop(0))

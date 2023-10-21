from collections import deque
import sys

T = int(sys.stdin.readline()) # 테스트 케이스의 수
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split()) # 문서의 개수, 몇번째로 인쇄되었는 지 궁금한 문서가 현재 Queue에 몇번째 놓여 있는지 나타내는 정수

    documents = list(map(int, sys.stdin.readline().split()))
    # 인덱스와 중요도를 저장하는 리스트로 재생성
    documents = deque([[idx, documents[idx]] for idx in range(len(documents))])

    print_count = 0
    while len(documents) > 0:
        another_priority = [documents[idx][1] for idx in range(1, len(documents))]
        if len(another_priority) > 0 and documents[0][1] < max(another_priority):
            documents.append(documents.popleft())
        else:
            print_count += 1

            if documents[0][0] == M:
                print(print_count)
                break
            else:
                documents.popleft()

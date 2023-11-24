import sys

N = int(input()) # 설탕 중량

bag = 0
while N >= 0:
    if N % 5 == 0: # 5의 배수이면
        bag += (N // 5) # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break

    N -= 3
    bag += 1

else:
    print(-1)
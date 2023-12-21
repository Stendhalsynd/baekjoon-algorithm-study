from itertools import permutations

n = int(input())

oneToNine = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # 인덱스로 접근하기 쉽게 string 형식으로 1~9 숫자 저장
available = list(permutations(oneToNine, 3))  # 순서 고려하여 중복 없이 뽑을 수 있는 permutations 사용하여 가능한 숫자 3개 뽑음

for _ in range(n):
    num, strike, ball = map(int, input().split())
    num = str(num)
    removes = 0  # 지워진 숫자 만큼의 수를 셈 (지워주지 않으면 Index Error가 남)
    for i in range(len(available)):
        i -= removes  # i에서 지워진 숫자만큼 셈
        strikes, balls = 0, 0
        for j in range(3):
            if available[i][j] == num[j]:  # 만약 숫자가 동일한 자리에 위치하면 strikes += 1
                strikes += 1
            elif num[j] in available[i]:  # 만약 숫자가 존재하기는 하지만 자리는 다르다면 balls += 1
                balls += 1
        if strikes != strike or balls != ball:  # 주어진 strike와 계산한 strikes와 다르거나, 주어진 ball과 계산한 balls가 다르면 
            available.remove(available[i])   # available(위에서 뽑은 숫자 순열 리스트)에서 다른 숫자 삭제
            removes += 1  # i에서 지울 숫자에 += 1 해줌
print(len(available))  # 남은 available의 리스트 길이가 답이 됨

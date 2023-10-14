import sys

# 입력값 받기
n = int(input()) # 첫째 줄에는 자연수의 개수 N
data = list(map(int, input().split())) # 둘째 줄에는 N개의 자연수가 빈칸을 사이에 두고 입력

# 더한 결과값 리스트에 넣기 위해
ans_list =[]

# 인덱스 0번을 기준으로 n번까지 빼야하니까 이중 for문 이용
for i in range (0, n):
    result = 0 # 인덱스 번호 마다 계산한 값을 넣어야 하기 지역변수 선언
    for j in range(1, n):
        result = result + abs(data[i] - data[j]) # 인덱스 0번을 기준으로 1,2..n번까지 뺀 결과값을 절대값으로 넣기
    ans_list.append(result) # 인덱스 0번을 기준으로 n번까지 뺀 결과값을 list에 넣어줌

# result 값이 가장 작은 수를  뽑기 위해 min 사용, min 값의 인덱스 번호 이용하여 출력
print(data[ans_list.index(min(ans_list))])
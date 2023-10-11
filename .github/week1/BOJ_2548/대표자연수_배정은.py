import sys

def difference_number_sum(idx, numbers):
    number_sum = 0
    for num in numbers:
        number_sum += abs(num - numbers[idx]) # 다른 자연수의 차를 모두 더함
    return number_sum

N = int(sys.stdin.readline().rstrip()) # N값 입력
numbers = sorted(list(map(int, sys.stdin.readline().split()))) # 오름차순으로 정렬하기

# 중앙 위치한 값 인덱스 저장
left, right = 0, 0
if len(numbers) % 2 == 1: # 배열 크기가 홀수일 경우에
    left, right = len(numbers) // 2, len(numbers) // 2
else: # 짝수일때
    left, right = (len(numbers) // 2) - 1, len(numbers) // 2

min_difference_sum = [0, left]
for idx in range(len(numbers) // 2): # 중간부터 확인
    left_difference_sum, right_difference_sum = difference_number_sum(left, numbers), difference_number_sum(right, numbers)

    if idx == 0:
            min_difference_sum = [left_difference_sum, left] if left_difference_sum <= right_difference_sum else [right_difference_sum, right]
    else:
        if min_difference_sum[0] > left_difference_sum:
            min_difference_sum = [left_difference_sum, left]
        else:
            break

        if min_difference_sum[0] > right_difference_sum:
            min_difference_sum = [right_difference_sum, right]

    left, right = left - 1, right + 1  # 중간부터 하나씩 더해서 인덱스 이동
print(numbers[min_difference_sum[1]])
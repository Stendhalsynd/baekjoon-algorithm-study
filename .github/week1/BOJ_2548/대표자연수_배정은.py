import sys

def difference_number_sum(n, numbers):
    number_sum = 0
    for num in numbers:
        number_sum += abs(num - n) # 다른 자연수의 차를 모두 더함
    return number_sum

N = int(sys.stdin.readline().rstrip()) # N값 입력
numbers = sorted(list(map(int, sys.stdin.readline().split()))) # 오름차순으로 정렬하기

if len(numbers) % 2 == 1: # 배열 크기가 홀수일 경우에
    print(numbers[len(numbers) // 2]) # 중앙 위치한 값 출력
else: # 짝수일때
    # 중간에서 작은 값이 더 최소의 자연수의 합이면 출력, 아닐 경우 중간에서 큰 값을 출력
    # 만약 같으면 작은 값이 출력
    print(numbers[(len(numbers) // 2) - 1] if difference_number_sum((len(numbers) // 2) - 1, numbers) < difference_number_sum(len(numbers) // 2, numbers) else numbers[(len(numbers) // 2) - 1])
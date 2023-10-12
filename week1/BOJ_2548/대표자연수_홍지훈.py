N = int(input())
numbers = [int(x) for x in input().split()]

numbers.sort()

if N % 2 == 0:
    print(numbers[N // 2 - 1])
else:
    print(numbers[N // 2])

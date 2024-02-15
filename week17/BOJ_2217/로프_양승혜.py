n = int(input())
count = 1
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse = True) # 굳이 내림차순으로 정렬하지 않아도 되긴 함

answer = []
for num in nums:
    answer.append(num * count)
    count += 1

print(max(answer))
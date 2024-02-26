n = int(input())
count = 1
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort(reverse = True)

answer = []
for num in nums:
    answer.append(num * count)
    count += 1

print(max(answer))

from itertools import permutations

a, b = input().split()

if len(b) < len(a): # b의 자리수가 a의 자리수보다 짧으면 무조건 -1
    print(-1)

else:
    numList = list(permutations(a))
    nums = []
    for num in numList:
        if num[0] != '0': # 0으로 시작하는 숫자 제외한 나머지 숫자들 append
            nums.append("".join(num))
    nums.sort(reverse = True) # 숫자가 큰 순서로 정렬
    if nums[-1] > b: # 정렬된 숫자들 중 가장 끝 수(가장 작은 수)가 b보다 작으면 무조건 -1
        print(-1)
    else:
        for num in nums: # 아니라면, 작은 숫자가 발견되는 즉시 print하고 break
            if int(num) < int(b):
                print(int(num))
                break

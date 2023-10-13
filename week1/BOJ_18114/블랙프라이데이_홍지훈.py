import sys
import bisect


def findResult(nums, C, N):
    # 1개가 존재할 때
    if bisect.bisect_left(nums, C) < N:
        return 1
    i = 0
    j = N - 1
    while i < j:
        sum = nums[i] + nums[j]
        if C < sum:  # i, j 고른게 너무 클때 값을 감소시킨다.
            j -= 1
        elif C == sum:  # 2개일 때
            return 1
        else:  # i, j 고른게 너무 작을때 값을 증가시킨다.
            diff = C - sum
            if findThirdVal(nums, i, j, diff):  # 중간값이 nums 에 있는지 확인한다
                return 1
            i += 1
    return 0


def findThirdVal(nums, i, j, diff):
    index = bisect.bisect_left(nums, diff)
    if (
        diff != nums[i]
        and diff != nums[j]
        and i < index < j
        and nums[i] < nums[index] < nums[j]
    ):
        return 1
    return 0


# 문자열 입력받기
N, C = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

output = 0

nums.sort()  # 물건의 무게를 정렬

output = findResult(nums, C, N)

print(output)

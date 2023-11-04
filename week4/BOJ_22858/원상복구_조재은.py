import sys

n,k = map(int, input().split())
sList = list(map(int, input().split()))
dList_temp = list(map(int, input().split()))

dList = []
for i in range(n):
    dList.append([dList_temp[i],i])

print(dList) # [[4, 0], [3, 1], [1, 2], [2, 3], [5, 4]]

# 5 2
# 4 1 3 5 2
# 4 3 1 2 5

dList.sort()

print(dList) # [[1, 2], [2, 3], [3, 1], [4, 0], [5, 4]]

ans = [sList[i] for i in range(n)] # [4, 1, 3, 5, 2]

for i in range(k):
    temp = []
    # [3, 5, 1, 4, 2]
    for d in dList:
        temp.append(ans[d[1]])
        print("d:", d[1], ans[d[1]])
    for j in range(n):
        ans[j] = temp[j]

print(*ans)
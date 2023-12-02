# 1. greedy
total = int(input())
bag = 0

# total이 0보다 클 때까지만 while문 작동
# 5로 나눈 나머지가 0이라면 bag에 5로 나눈 몫을 더하고, bag를 print하고, break를 통해 while문을 빠져나온다.
# while문을 빠져나오지 못했다면 total에서 3을 빼고, bag에 1을 더한다
while total >= 0:
    if total % 5 == 0:
        bag += total // 5
        print(bag)
        break
    total -= 3
    bag += 1

# 만약 whlie문에서 break가 실행되지 않으면 -1을 print 한다.
else:
    print(-1)

# 2. dp
n = int(input())
sugar = [-1] * (n + 1)

for i in range(3, len(sugar)):
    if i == 3 or i == 5:
        sugar[i] = 1
    elif sugar[i - 3] < 0 and sugar[i - 5] < 0:
        sugar[i] = -1
    elif sugar[i - 3] > 0 and sugar[i - 5] > 0:
        sugar[i] = 1 + min(sugar[i - 3], sugar[i - 5])
    else:
        sugar[i] = 1 + max(sugar[i - 3], sugar[i - 5])

print(sugar[n])

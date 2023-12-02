n = int(input())

big = n // 5
small = 0

while True:    

    if (n - big * 5) % 3 == 0:
        small = (n - big * 5) // 3
        print(big+small)
        break

    big -= 1

    if big < 0 :
        print(-1)
        break
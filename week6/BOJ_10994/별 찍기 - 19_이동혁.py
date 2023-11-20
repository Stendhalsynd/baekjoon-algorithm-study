n = int(input())

line = 1 + 4 * (n - 1)

if line == 1:
    print('*')
else:
    # 첫째 줄
    for _ in range(line):
        print('*', end = '')

    print()

    # 둘째 줄 ~ 중간 줄 이전까지
    for i in range(int((line - 3) / 2)):
        if i % 2 == 0:
            for _ in range(int(i // 2) + 1):
                print('* ', end = '')
            for _ in range(int(line - (i // 2) * 2 * 2) - 3):
                print(' ', end = '')
            for _ in range(int(i // 2)):
                print('* ', end = '')
            print('*', end = '')
            print()
        if i % 2 == 1:
            for _ in range(int(i//2) + 1):
                print('* ', end = '')
            for _ in range(int(line - (i // 2) * 2 * 2) - 4):
                print('*', end = '')
            print(' ', end = '')
            for _ in range(int(i // 2)):
                print('* ', end = '')
            print('*', end = '')
            print()
            
    # 중간 줄
    for _ in range(int(line//2) + 1):
        print('* ', end = '')
    print()

    # 중간 줄 이후 ~ 마지막 줄 이전까지
    for i in range(int((line - 3) / 2), 0, - 1):
        if i % 2 == 1:
            for _ in range(int(i // 2) + 1):
                print('* ', end = '')
            for _ in range(int(line - (i // 2) * 2 * 2) - 3):
                print(' ', end = '')
            for _ in range(int(i // 2)):
                print('* ', end = '')
            print('*', end = '')
            print()
        if i % 2 == 0:
            for _ in range(int(i//2)):
                print('* ', end = '')
            for _ in range(int(line - (i // 2) * 2 * 2) ):
                print('*', end = '')
            print(' ', end = '')
            for _ in range(int(i // 2) - 1):
                print('* ', end = '')
            print('*', end = '')
            print()

    for _ in range(line):
        print('*', end = '')
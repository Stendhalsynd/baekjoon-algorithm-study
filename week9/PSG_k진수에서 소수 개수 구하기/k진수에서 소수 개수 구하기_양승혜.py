def change(number, to):
    result = ""
    while number:
        number, remain = divmod(number, to)
        result = str(remain) + result
    return result

def solution(n, k):
    answer = 0
    newN = change(n, k)
    split = newN.split("0")
    for strnum in split:
        if not strnum or int(strnum) == 1:
            continue
        error = 0
        for i in range(2, int(int(strnum) ** 0.5) + 1):
            if int(strnum) % i == 0:
                error += 1
        if error == 0:
            answer += 1

    return answer

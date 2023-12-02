from itertools import product

def solution(users, emoticons):
    answer = []
    percents = [10, 20, 30, 40]
    for cases in product(percents, repeat = len(emoticons)):
        result = [0, 0]
        for user in users:
            pay = 0
            for idx, percent in enumerate(cases):
                if user[0] <= percent:
                    pay += emoticons[idx] * (100 - percent) // 100
            if pay >= user[1]:
                result[0] += 1
            else:
                result[1] += pay
        answer.append(result)
    answer.sort(key = lambda x: (-x[0], -x[1]))
    return answer[0]

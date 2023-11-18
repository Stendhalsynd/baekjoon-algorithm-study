def solution(users, emoticons):
    answer = [0,0]
    data = [10, 20, 30, 40]
    discount = []
    def dfs(tmp, d): # 모든 경우의 할인율 조합을 구함
        if d == len(tmp):
            discount.append(tmp[:])
            return
        else:
            for i in data:
                tmp[d] += i
                dfs(tmp, d+1)
                tmp[d] -= i
    dfs([0]*len(emoticons), 0)
    for disc in discount: # 만들어진 모든 조합을 하나씩 살펴봄
        cnt = 0
        get = 0
        for i in users:
            pay = 0
            for j in range(len(disc)):
                if i[0] <= disc[j]:
                    pay += emoticons[j] * (100 - disc[j])/100
                if pay >= i[1]:
                    break
            if pay >= i[1]:
                pay = 0
                cnt += 1
            get += pay
        if cnt >= answer[0]:
            if cnt == answer[0]:
                answer[1] = max(answer[1], get)
            else:
                answer[1] = get
            answer[0] = cnt
    return answer
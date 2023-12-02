from itertools import product

def solution(users, emoticons):
    answer = [-1, -1] # [가입자 수, 이모티콘 매출액]
    
    for discounts in product([10, 20, 30, 40], repeat=len(emoticons)):
        total_cost = 0
        new_users = 0
        
        for user in users:
            user_cost = 0
        
            for i in range(len(discounts)):
                if discounts[i] >= user[0]:
                    user_cost += emoticons[i] * (1 - discounts[i] / 100)
                    
            if user_cost >= user[1]:
                new_users += 1
            else:
                total_cost += user_cost
                
        answer = max(answer, [new_users, total_cost])
    
    return answer
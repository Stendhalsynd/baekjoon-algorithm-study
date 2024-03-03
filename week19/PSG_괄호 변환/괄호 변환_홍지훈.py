def is_balanced(p):
    count = 0
    for char in p:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:  # '('보다 ')'가 많이 나왔을 때 -> 균형이 깨진 경우
            return False
    return count == 0 # '(' 와 ')' 의 쌍의 수가 같게 나왔을 때

def solution(p):
    # 1. 빈문자는 바로 반환
    if not p: return ""

    # 2. is_balanced 가 True 가 되려면 괄호의 수도 같고 짝도 맞아야 한다.
    if is_balanced(p): return p

    count = 0
    for i in range(len(p)):
        # 닫는 괄호, 여는 괄호의 수 카운트
        if p[i] == '(': count += 1
        else: count -= 1
        
        # 균형잡힌 괄호 문자열이 나올 경우 u, v 를 구해 반복문 탈출
        if count == 0: 
            u = p[:i+1]
            v = p[i+1:]
            break

    # 3. 만약 쪼갠 u가 올바른 괄호 문자열이라면 나머지 v 에 위의 과정을 반복해 u 에 이어 붙인다.
    if is_balanced(u): return u + solution(v)

    # 4. 첫 번째 문자로 "(" 를 붙이고 v 에 대해 solution 을 수행한 결과에 이어 ")" 를 붙인다.
    else: 
        answer = '(' + solution(v) + ')'
        for char in u[1:-1]: # u 의 첫, 마지막 문자 제거후 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
            if char == '(':
                answer += ')'
            else:
                answer += '('
        return answer
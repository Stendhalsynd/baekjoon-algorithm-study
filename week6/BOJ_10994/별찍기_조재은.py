import  sys

# 재귀함수 사용
def add_star(ptn):
    return "* " + ptn + " *"

def star(n):
    if n == 1:
        return ["*"]
    else:
        # 첫줄, 마지막줄 : (4*n-3)
        # 공백 : (4*n-5)
        # star(n)은 가장 바깥쪽 행을 생성하고, 그 다음 star(n-1)을 호출하여 중간 부분 생성 후, 마지막으로 바깥쪽 행을 반복합니다.
        # 이 중간 부분을 생성할 떄 'add_star' 함수가 각 줄에 적용되어 양쪽에 별과 공백 추가
        return ["*"*(4*n-3), "*" + " " * (4*n-5) + "*"]\
                + list(map(add_star, star(n-1)))\
                + ["*" + " "*(4*n-5) + "*", "*"*(4*n-3)]

print("\n".join(star(int(input())))) # 입력값, 출력값
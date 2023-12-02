strings = input()
stack = []
answer = ""
flag = False

for string in strings:

    if string == "<":
        flag = True
        while stack:
            answer += stack.pop()
        answer += "<"

    elif string == ">":
        flag = False
        answer += string

    elif string == " " and not flag:
        while stack:
            answer += stack.pop()
        answer += string
    
    elif flag:
        answer += string
    
    else:
        stack.append(string)

while stack:
    answer += stack.pop()
    
print(answer)

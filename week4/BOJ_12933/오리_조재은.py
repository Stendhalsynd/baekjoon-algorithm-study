import sys

string = list(input()) # 오리 울음 입력
count = 0 # 오리 수

# 올바르지 않은 경우 출력
# 문자열이 "q"로 시작하고, "k"로 끝나며 길이가 5의 배수인지 확인
if string[0] != "q" or string[-1] != "k" or len(string) % 5:
    print(-1)
    exit()

def find_quack(start):
    quack = "quack" # 찾고자 하는 문자열
    j = 0 # 현재 탐색 중인 'quack' 문자열의 인덱스를 나타냄
    global count
    new_ori = True # 새로운 오리 패턴을 시작하는지 여부를 나타내는 플래그

    for i in range(start, len(string)): # 문자열 탐색
        if string[i] == quack[j]: # 현재 문자가 탐색 중인 문자와 일치하는지 확인
            if string[i] == "k": # 현재 문자가 "k"이면 새로운 오리 패턴인지 확인하고, 새로운 오리이면 count + 1 한다.
                if new_ori:
                    count += 1
                    new_ori = False
                j = 0
                string[i] = 0
                continue
            # 일치하는 문자를 0으로 바꾸고 'quack' 패턴의 인덱스 'j'를 1 증가시켜 다음 문자 탐색
            j += 1
            string[i] = 0

# "q" 문자 뒤에는 "uack"가 와야 하므로, 문자열의 끝에서 4글자 이전 까지만 검사를 진행
# 이렇게 하면 문자열 끝 부분에서 불필요한 검사를 방지할 수 있음
for i in range(len(string) - 4):
    if string[i] == "q": # 문자열에서 "q"문자를 발견할 때마다 찾기 시작!
        find_quack(i)

# any(string)은 리스트 내에 하나 이상의 true 값이 있는지 확인하는 함수
# 변환되지 않은 문자가 있으면 'True', 모드 변환되었으면 'False'
if any(string) or count == 0:
    print(-1)
else:
    print(count)
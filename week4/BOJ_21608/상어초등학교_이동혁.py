n = int(input())
student_list = [list(map(int, input().split())) for _ in range(n**2)]

seat_matrix = [[None for _ in range(n)] for _ in range(n)]

seat_matrix[1][1] = student_list[0][0]

def find_seat_condition1(lst):
    answer = []
    board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if seat_matrix[i][j] == None:
                if i-1 >= 0 and seat_matrix[i-1][j] in lst[1:]:
                    board[i][j] += 1
                if i+1 < n and seat_matrix[i+1][j] in lst[1:]:
                    board[i][j] += 1
                if j-1 >= 0 and seat_matrix[i][j-1] in lst[1:]:
                    board[i][j] += 1
                if j+1 < n and seat_matrix[i][j+1] in lst[1:]:
                    board[i][j] += 1
    
    max = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > max:
                max = board[i][j]
        
    for i in range(n):
        for j in range(n):
            if board[i][j] == max and seat_matrix[i][j] == None:
                answer.append([i, j])
    return answer

def find_seat_condition2(lst):
    answer = []
    vacant = []
    for index in lst:
        total = 0
        if index[0]-1 >= 0 and seat_matrix[index[0]-1][index[1]] == None:
            total += 1
        if index[0]+1 < n and seat_matrix[index[0]+1][index[1]] == None:
            total += 1
        if index[1]-1 >= 0 and seat_matrix[index[0]][index[1]-1] == None:
            total += 1
        if index[1]+1 < n and seat_matrix[index[0]][index[1]+1] == None:
            total += 1
        vacant.append(total)

    max_num = max(vacant)

    for i in range(len(vacant)):
        if vacant[i] == max_num:
            answer.append(lst[i])
    return answer

def find_sear_condition3(lst):
    answer = []

    min_num = 100
    for index in lst:
        if index[0] < min_num:
            min_num = index[0]
    
    for index in lst:
        if index[0] == min_num:
            answer.append(index)

    return answer

def find_seat_condition4(lst):
    answer = []

    min_num = 100

    for index in lst:
        if index[1] < min_num:
            min_num = index[1]
    
    for index in lst:
        if index[1] == min_num:
            answer.append(index)

    return answer

for i in range(1, n**2):
    condition1 = find_seat_condition1(student_list[i])
    if len(condition1) == 1:
        seat_matrix[condition1[0][0]][condition1[0][1]] = student_list[i][0]
    else:
        condition2 = find_seat_condition2(condition1)
        if len(condition2) == 1:
            seat_matrix[condition2[0][0]][condition2[0][1]] = student_list[i][0]
        else:
            condition3 = find_sear_condition3(condition2)
            if len(condition3) == 1:
                seat_matrix[condition3[0][0]][condition3[0][1]] = student_list[i][0]
            else:
                condition4 = find_seat_condition4(condition3)
                seat_matrix[condition4[0][0]][condition4[0][1]] = student_list[i][0]

def find_index(value):
    for i in range(n):
        for j in range(n):
            if seat_matrix[i][j] == value:
                return [i, j]
            
score = 0
for i in range(n**2):
    total = 0
    student_number = student_list[i][0]
    seat_index = find_index(student_number)
    if seat_index[0]-1 >= 0 and seat_matrix[seat_index[0]-1][seat_index[1]] in student_list[i][1:]:
        total += 1
    if seat_index[0]+1 < n and seat_matrix[seat_index[0]+1][seat_index[1]] in student_list[i][1:]:
        total += 1
    if seat_index[1]-1 >= 0 and seat_matrix[seat_index[0]][seat_index[1]-1] in student_list[i][1:]:
        total += 1
    if seat_index[1]+1 < n and seat_matrix[seat_index[0]][seat_index[1]+1] in student_list[i][1:]:
        total += 1
    
    if total == 0:
        score += 0
    if total == 1:
        score += 1
    if total == 2:
        score += 10
    if total == 3:
        score += 100
    if total == 4:
        score += 1000
    
print(score)

        
    


    


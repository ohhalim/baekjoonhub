def solution(keyinput, board):
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    
    location = [0, 0]
    for i in keyinput:
        if i == "left":
            if location[0] > -max_x:
                location[0] -= 1 # 인덱스 위치에 넣는구나
        elif i == "right":
            if location[0] < max_x:
                location[0] += 1
        elif i == "up":
            if location[1] < max_y:
                location[1] += 1
        elif i == "down":
            if location[1] > -max_y:
                location[1] -= 1
        
    return location
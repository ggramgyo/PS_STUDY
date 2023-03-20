def solution(board):
    answer = 0
    O, X, dot = 0, 0, 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == 'O':
                O += 1
            if board[x][y] == 'X':
                X += 1
    # 게임이 정상적으로 진행되는 경우는 두가지로 나눠보자
        # O가 X보다 한가지 많은 경우
            # 게임 정상 진행 경우 -> X가 로직을 완성한 경우를 제외한 모두
        # O와 X가 같은 경우
            # 게임 정상 진행 경우 -> O가 로직을 완성한 경우를 제외한 모두
    if O - 1 == X:
        answer = 1
        # 대각선 경우
        if board[0][0] == 'X' and board[0][0] == board[1][1] == board[2][2]:
            answer = 0

        if board[2][0] == 'X' and board[0][2] == board[1][1] == board[2][0]:
            answer = 0
        # 가로 세로
        for i in range(3):
            if board[0][i] == 'X' and board[0][i] == board[1][i] == board[2][i]:
                answer = 0
            if board[i][0] == 'X' and board[i][0] == board[i][1] == board[i][2]:
                answer = 0
    if O == X:
        answer = 1
        # 대각선 경우
        if board[0][0] == 'O' and board[0][0] == board[1][1] == board[2][2]:
            answer = 0

        if board[2][0] == 'O' and board[0][2] == board[1][1] == board[2][0]:
            answer = 0
        # 가로 세로
        for i in range(3):
            if board[0][i] == 'O' and board[0][i] == board[1][i] == board[2][i]:
                answer = 0
            if board[i][0] == 'O' and board[i][0] == board[i][1] == board[i][2]:
                answer = 0
    return answer

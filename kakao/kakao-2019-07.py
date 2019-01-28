# https://www.welcomekakao.com/learn/courses/30/lessons/42894?language=python3
'''
board를 돌면서 지울 수 있는 block을 다 지워봄
특히 block을 지운 후에 그 다음 위치만 보는 것이 아니라 다시 처음부터 봐야
새로 지울 수 있는 block을 확인할 수 있음
'''


def can_remove_2by3(board, i, j):
    N = len(board[0])
    if i+1<N and j+2<N:
        # o x x
        # o o o
        if board[i][j] != 0:
            # 위에가 빈칸인지 확인
            column1 = [row[j+1] for row in board][:i]
            column2 = [row[j+2] for row in board][:i]
            if sum(column1) > 0 or sum(column2) > 0:
                return False

            # 블록 모양이 삭제 가능한지 확인
            block_number = board[i][j]
            if board[i+1][j] == board[i+1][j+1] == board[i+1][j+2] == block_number and board[i][j+1] == board[i][j+2] == 0:
                return True

            else:
                return False

        # x o x
        # o o o
        if board[i][j+1] != 0:
            # 위에가 빈칸인지 확인
            column1 = [row[j] for row in board][:i]
            column2 = [row[j+2] for row in board][:i]
            if sum(column1) > 0 or sum(column2) > 0:
                return False

            # 블록 모양이 삭제 가능한지 확인
            block_number = board[i][j+1]
            if board[i+1][j] == board[i+1][j+1] == board[i+1][j+2] == block_number and board[i][j] == board[i][j+2] == 0:
                return True

            else:
                return False

        # x x o
        # o o o
        if board[i][j+2] != 0:
            # 위에가 빈칸인지 확인
            column1 = [row[j] for row in board][:i]
            column2 = [row[j+1] for row in board][:i]
            if sum(column1) > 0 or sum(column2) > 0:
                return False

            # 블록 모양이 삭제 가능한지 확인
            block_number = board[i][j+2]
            if board[i+1][j] == board[i+1][j+1] == board[i+1][j+2] == block_number and board[i][j] == board[i][j+1] == 0:
                return True

            else:
                return False

    else:
        return False

def can_remove_3by2(board, i, j):
    N = len(board[0])
    if i+2<N and j+1<N:
        # o x
        # o x
        # o o
        if board[i][j] != 0:
            # 위에가 빈칸인지 확인
            column1 = [row[j+1] for row in board][:i]
            if sum(column1) > 0:
                return False

            # 블록 모양이 삭제 가능한지 확인
            block_number = board[i][j]
            if board[i+1][j] == board[i+2][j] == board[i+2][j+1] == block_number and board[i][j+1] == board[i+1][j+1] == 0:
                return True

            else:
                return False

        # x o
        # x o
        # o o
        if board[i][j+1] != 0:
            # 위에가 빈칸인지 확인
            column1 = [row[j] for row in board][:i]
            if sum(column1) > 0:
                return False

            # 블록 모양이 삭제 가능한지 확인
            block_number = board[i][j+1]
            if board[i+1][j+1] == board[i+2][j] == board[i+2][j+1] == block_number and board[i][j] == board[i+1][j] == 0:
                return True

            else:
                return False

    else:
        return False


def remove_2by3(board, i, j):
    copied = [row for row in board]
    for _i in range(i, i+2):
        for _j in range(j, j+3):
            copied[_i][_j] = 0

    return copied


def remove_3by2(board, i, j):
    copied = [row for row in board]
    for _i in range(i, i+3):
        for _j in range(j, j+2):
            copied[_i][_j] = 0

    return copied

# 지울 수 있는 사각형은 총 5가지 종류가 있음
# 모든 block을 돌면서 2x3직사각형, 3x2직사각형 범위를 지울 수 있는지 확인
def solution(board):
    arr = []
    N = len(board[0])

    for i in range(N):
        for j in range(N):
            if can_remove_2by3(board, i, j):
                removed = remove_2by3(board, i, j)
                arr.append(1 + solution(removed))

            if can_remove_3by2(board, i, j):
                removed = remove_3by2(board, i, j)
                arr.append(1+ solution(removed))

    if len(arr) == 0:
        return 0
    else:
        return max(arr)

board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
print(solution(board))
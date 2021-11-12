import numpy as np

counter = 0

def checkDiagonals(board, x, y, i):
    if x+i < 8 and y+i < 8:
        if board[x+i, y+i] == 1:
            return 1
    if x-i >= 0 and y+i < 8:
        if board[x-i, y+i] == 1:
            return 1
    if x-i >= 0 and y-i >= 0:
        if board[x-i, y-i] == 1:
            return 1
    if x+i < 8 and y-i >= 0:
        if board[x+i, y-i] == 1:
            return 1
    return 0

def queens(x, y, board):
    aux = 0
    if x == 8:
        global counter
        counter += 1
        print(counter)
        print(board)
        return 0
    for y in range(8):
        for i in range(8):
            if board[x,i] == 1 or board[i,y] == 1 or checkDiagonals(board, x, y, i) == 1:
                aux = 1
                break
        if aux == 0:
            board[x,y] = 1
            if queens(x+1, 0, board) == 0:
                board[x,y] = 0
            else:
                return 1
        aux = 0
    return 0

def queensLeft(x, y, board):
    aux = 0
    if y == -1:
        global counter
        counter +=1
        print(counter)
        print(board)
        return 0
    for x in range(8):
        for i in range(8):
            if board[x,i] == 1 or board[i,y] == 1 or checkDiagonals(board, x, y, i) == 1:
                aux = 1
                break
        if aux == 0:
            board[x,y] = 1
            if queensLeft(0, y-1, board) == 0:
                board[x,y] = 0
            else:
                return 1
        aux = 0
    return 0

def main():
    board = np.zeros( (8,8) )
    # start position 0x0, recursive solution increasing the x axis by 1 each time
    queens(0, 0, board)

    global counter
    counter = 0
    board = np.zeros( (8,8) )
    # start position 0x7, recursive solution decreasing the y axis by 1 each time
    queensLeft(0, 7, board)        

if __name__ == "__main__":
    main()
# criar uma matriz do tamanho da primeira casa
sudokuBoard = [
    [0, 0, 0, 0, 0, 0, 5, 0, 9],
    [8, 0, 0, 0, 7, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 9, 3, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [6, 7, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 0, 2, 0, 3, 0, 0, 0],
    [4, 0, 0, 9, 0, 0, 0, 0, 0],
]

# função que resolve
def Resolve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row , column = find

    for i  in range(1,10):
        if valid(board , i , (row , column)):
            board[row][column] = i

            if Resolve(board):
                return True
            board[row][column] = 0
    return False

    

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[i])):
            if bo[i][j] == 0:
                return (i , j) #return row and column
    return None

def valid(bo , num , posi):
    # verica linha
    for i in range(len(bo[0])):
        if bo[posi[0]][i] == num and posi[1] != i:
            return False
        
    #verifica coluna
    for j in range(len(bo[0])):
        if bo[j][posi[1]] == num and posi[0] != j:
            return False
        
    # verifica quadrante
    quad_x = posi[1] // 3 
    quad_y = posi[0] // 3 
    for i in range(quad_y * 3 , quad_y * 3 + 3):
        for j in range(quad_x *3 , quad_x*3 + 3):
            if bo[i][j] == num and (i,j) != posi:
                return False
            
    return True


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- " * 15)
        for j in range(len(board[0])):
            if j % 3 == 0 and j !=0:
                print(" | " , end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + "  " , end="")




print_board(sudokuBoard)
Resolve(sudokuBoard)
print("-=" * 20)
print_board(sudokuBoard)

import numpy as np
def place_trimino(i, j, z, board, block):
  h, w = board.shape
  if z == 0:
    if block[1]+i > h or block[2]+j > w:
      return None
    for d in range(i, block[1]+i):
      if board[d][j] != 0:
        return None
      else:
        board[d][j]=block[3]
    for k in range(j+1, block[2]+j):
      if board[i][k]!= 0:
        return None
      else:
        board[i][k] = block[3]
  if z == 1:
    if block[1]+j > w or i - block[2] < -1:
      return None
    for d in range(i, i - block[2], -1):
      if board[d][j] != 0:
        return None
      else:
        board[d][j]=block[3]
    for k in range(j+1, block[1]+j):
      if board[i][k] != 0:
        return None
      else:
        board[i][k] = block[3]
  if z == 2:

    if i - block[1] < -1 or j - block[2] < -1:
      return None
    for d in range(i, i - block[1], -1):
      if board[d][j] != 0:
        return None
      else:
        board[d][j]=block[3]
    for k in range(j-1, j - block[2], -1):
      if board[i][k] != 0:
        return None
      else:
        board[i][k] = block[3]
  if z == 3:
    if j - block[1] < -1 or block[2]+i > h:
      return None
    for d in range(i, block[2]+i):
      if board[d][j] != 0:
        return None
      else:
        board[d][j]=block[3]
    for k in range(j-1, j - block[1], -1):
      if board[i][k] != 0:
        return None
      else:
        board[i][k] = block[3]
  return board

def place_square(i, j, z, board, block):
  h, w = board.shape
  if z == 0:
    if block[1]+j > w or block[2]+i > h or block[2]>block[1]:
      return None
    for d in range(i, block[2]+i):
      for k in range(j, block[1]+j):
        if board[d][k] != 0:
          return None
        else:
          board[d][k] = block[3]
  return board


def check_sizes(all_mino, board):
  #print(board)
  h,w = board.shape
  for (ind,block) in enumerate(all_mino):
    #print(block)
    for i in range(h):
      for j in range(w):
        board_prev = board.copy()
        if block[0] == 0:
          for z in range(1):
            board_new = place_square(i, j, z, board_prev, block)
            if type(board_new) == np.ndarray:
              new_all_mino = all_mino.copy()
              del new_all_mino[ind]
              
                #print(board_new)
              if len(new_all_mino) == 0:
                print('Final_board: ')
                print(board_new)
                return True

              flag = check_sizes(new_all_mino, board_new)
              if flag == True:
                return flag
          board_new = None
        if block[0] == 1:

          for z in range(4):
            board_new = place_trimino(i, j, z, board_prev, block)
            if type(board_new) == np.ndarray:
              new_all_mino = all_mino.copy()
              del new_all_mino[ind]
              if len(new_all_mino) == 0:
                print('Final_board: ')
                print(board_new)
                return True
              flag = check_sizes(new_all_mino, board_new)
              if flag == True:
                return flag
            board_new = None
    board_new = None
    board_prev = None
  return False
  
if __name__=="__main__":
  size = eval(input())
  #size = (4,5)
  #squares = [((2,2),2), ((1,1),3)]
  #triminos = [((3,2),1), ((2,2),2)]
  board = np.zeros((size[1], size[0]))
  squares = eval(input())
  triminos = eval(input())
  all_mino = []

  for square in squares:
    for d in range(square[1]):
      all_mino.append([0]+list((square[0][1], square[0][0])))

  for trimino in triminos:
    for d in range(trimino[1]):
      all_mino.append([1]+list(trimino[0]))

  for i in range(len(all_mino)):
    all_mino[i].append(i+1)
  #print("all_mino: ", all_mino)
  print(check_sizes(all_mino, board))

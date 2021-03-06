## A Board is a (listof (listof Str))
## Requires:
##   The length of the outer list is 10.
##   The length of each inner list is 10.
##   Each string is '.', 'L', or 'S'.

def empty_board():
    ## THIS IS FUNCTION IS PROVIDED TO HELP YOU TEST make_board.
    ## WE RECOMMEND THAT YOU DON'T CHANGE IT.
    '''
    Returns a list of lists representing a Snakes and Ladders
    board where each entry is a period.

    empty_board: None -> Board
    '''
    return list(map(lambda ignore: ["."] * 10, range(10)))

def populate(B,s_l,R,pos2):
    if R == []:
        return None
    elif pos2 >= len(R):
        return None
    else:
        row = 9 - ((R[pos2] - 1) // 10)
        if (1 <= R[pos2] <= 10) or (21 <= R[pos2] <= 30) or (41 <= R[pos2] <= 50) or (61 <= R[pos2] <= 70) or (81 <= R[pos2] <= 90):
            col = (R[pos2] - 1) % 10
        else:
            col = 9 - ((R[pos2] - 1) % 10)
        B[row][col] = s_l
        pos2 = pos2 + 1
        return populate(B, s_l, R, pos2)


def populate_snakes_ladders(B,s_l,lol,pos):
  if lol == []:
    return None
  elif pos >= len(lol):
    return None
  elif lol[pos] == []:
    pos = pos + 1
    return populate_snakes_ladders(B,s_l,lol,pos)
  else:
    Y = populate(B,s_l,lol[pos],0)
    pos = pos + 1
    return populate_snakes_ladders(B,s_l,lol,pos)


def make_board(snakes, ladders, board):
    X = populate_snakes_ladders (B,"S", snakes,0)
    X = populate_snakes_ladders (B,"L", ladders,0)
    return
'''
def print_board(B,pos3):
    if pos3 >= len(B):
        return None
    else:
        print (B[pos3])
        pos3 = pos3 + 1
        return print_board(B,  pos3)
'''
B = empty_board()
make_board([[1,20,21,40],[78,64],[50]],[[99,82,79,62,59],[47,53,69]],B)
#print_board(B,0)


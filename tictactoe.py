from pickle import TRUE

board = [["A1","A2","A3"],["B1","B2","B3"],["C1","C2","C3"]]
round = 0
hey = ''

game = 1
def show_board(nb):
    print("### Round ",round,"###")
    for x in board:
        print(x)
def state(player):
    no_empty = 0
    for x in board:
        oui = 0
        for e in x:
            if e == hey:
                oui +=1
            if oui == 3:
                print("The Game is Over, the player :",hey," Win the game")
                return 0
    for i  in range(3):
        oui = 0
        for e in range(3):
            if hey == board[e][i]:
                oui += 1
            if oui == 3:
                print("The Game is Over, the player :",hey," Win the game")
                return 0 
    if board[0][0] == hey:
        if board[1][1] == hey:
            if board[2][2] == hey:
                print("The Game is Over, the player :",hey," Win the game")
                return 0
    for x in board:
        for e in x:
            if e == 'X' or e == 'O':
                no_empty +=1
            if no_empty == 9:
                print("The Game is over Tie")
                return 0 
    return 1
def input_player():
    loop=1
    while loop == 1:
        index_ligne = -1
        index_colone = -1
        choose = input("choose your position for example A2 : ")
        if choose != 'X' or choose != 'O':
            for x in board:
                index_ligne +=1
                for e in x:
                    index_colone +=1
                    if e == choose:
                        while loop == 1:
                            res = input("Are your sure ? (y/n)")
                            if res == 'y':
                                board[index_ligne][index_colone] = hey
                                loop = 0
                                break
                            break
                index_colone = -1  
            index_colone = -1
            index_ligne = -1 

while(game):
    if round % 2 == 0:
        hey = 'X'
    else :
        hey = 'O'
    show_board(round)
    input_player()
    game = state(hey)
    
    round +=1
    
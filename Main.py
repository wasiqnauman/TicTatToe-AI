import Square
from MiniMax import MiniMax
from TicTacToeAction import TicTacToeAction
from TicTacToeState import TicTacToeState

if __name__ == '__main__':
    print("The squares are numbered as follows:")
    print("1|2|3\n-+-+-\n4|5|6\n-+-+-\n7|8|9\n")
    mark=False
    print("Do you want to use pruning? 1=no 2=yes ")
    use=(int)(input())
    if use == 2:
        mark=True
    print("Who should start? 1=you 2=computer ")
    temp =(int)(input())
    s = TicTacToeState()
    s.player = Square.X
    numMoves = 0
    if (temp == 1):
        s.playerToMove = Square.O
    else :
        s.playerToMove = Square.X
    while (numMoves < len(s.field)):
        numMoves += 1
        if (s.playerToMove == Square.X):
            minimax=MiniMax()
            s = s.getResult(minimax.MinimaxDecision(s, mark))
        else :
            print("Which square do you want to set? (1--9) ")
            while (True):
                temp = (int)(input())

                if  temp >= 1 & temp <= 9 :
                    if s.field[temp-1] != Square.EMPTY:
                        print("Square already filled, try again")
                        continue
                    else:
                        break
            a = TicTacToeAction(Square.O, temp - 1)
            print(f'Action: {a.position}, {a.player}')
            s = s.getResult(a)
        s.printresult()
        print(f'Ended: {s.isTerminal()}')
        if  s.isTerminal():
            break
    if (s.getUtility() > 0):
        print("You lost")
    elif (s.getUtility() < 0) :
        print("You win")
    else:
        print("Draw")

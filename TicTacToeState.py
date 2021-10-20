#class that implements a state and the playing logic of the TicTacToe game.
import Square
from TicTacToeAction import TicTacToeAction


class TicTacToeState:
    # Updates the utility value.
    def checkSameCol(self, matrix):
        sameCol = False
        color = None
        for i in range(3):
            found = True
            prev = matrix[0][i]
            if prev == Square.EMPTY:
                continue
            for j in range(1, 3):
                if prev != matrix[j][i]:
                    found = False
            if found:
                sameCol = True
                color = prev


        return [sameCol, color] if sameCol else None

    def checkSameRow(self, matrix):
        sameRow = False
        color = None
        for i in range(3):
            found = True
            prev = matrix[i][0]
            if prev == Square.EMPTY:
                continue
            for j in range(1, 3):
                if matrix[i][j] != prev:
                    found = False
                    break
            if found:
                sameRow = True
                color = prev

        return [sameRow, color] if sameRow else None


    def checkSameDiag(self, matrix):
        sameDiag = False
        # check diagonal L->R
        found1 = True
        prev = matrix[0][0]
        if prev == Square.EMPTY:
            found1 = False
        color = None
        for i in range(1,3):
            if matrix[i][i] != prev:
                found1 = False
                break

        if found1:
            sameDiag = True
            color = prev

        # check diagonal R->L
        n = len(matrix)
        prev = matrix[0][n-1]
        found2 = True
        if prev == Square.EMPTY:
            found2 = False

        for i in range(1,3):
            if matrix[i][n-1-i] != prev:
                found2 = False
                break

        if found2:
            sameDiag = True
            color = prev

        return [sameDiag, color] if sameDiag else None


    def updateUtility(self):
        print ("Updates the utility value.")
        # TODO The utility value for the TicTacToe game is defined as follows:
        #   - if player has three marks in a row, it is 1
        #   - if the other player has three marks in a row, it is -1
        #   - otherwise it is 0
        #   Note tha "three marks in a row" can actually be a row, a column
        #   or a diagonal.So basically, first find out if there are three
        #   identical values in a row, and if so, check whether the marks belong
        #   to player or not.

        # convert the field into a matrix for easy checking of rows/columns and diagonals
        fld = list(self.field)
        matrix = []
        for i in range(3):
            matrix.append(fld[:3])
            fld = fld[3:]
        # check rows
        sameRow = self.checkSameRow(matrix)
        # check cols
        sameCol = self.checkSameCol(matrix)
        # check diagonals
        sameDiag = self.checkSameDiag(matrix)



        if sameRow:
            if sameRow[1] == self.player:
                self.utility = 1
            else:
                self.utility = -1
        if sameCol:
            if sameCol[1] == self.player:
                self.utility = 1
            else:
                self.utility = -1
        if sameDiag:
            if sameDiag[1] == self.player:
                self.utility = 1
            else:
                self.utility = -1


    # Default constructor.
    def __init__(self):
        self.field = [] # < The field, consisting of nine squares.First three values correspond to first row, and so on.
        for i in range(9):
            self.field.append(Square.EMPTY)
        self.player = Square.X # < The player, either X or O.
        self.playerToMove = Square.X # < The player that is about to move.
        self.utility = 0 # < The utility value of this state.Can be 0, 1 (won) or -1 (lost).

    def getActions(self):
        #  TODO For the TicTacToe game, there is one valid action
        #   for each empty square.The action would then consist
        #   of the position of the empty square and the "color" of
        #   the player to move.
        print("getActions")
        #list=[]
        #return list
        actions = []
        for i in range(len(self.field)):
            if self.field[i] == Square.EMPTY:
                a = TicTacToeAction(self.playerToMove, i)
                actions.append(a)

        return actions


    def getUtility(self):
        return self.utility

    def getResult(self, action):
        #TODO Create a new state and copy all the contents of the current state
        #  to the new one (in particular the field and the player).
        # The player to move must be switched. Then incorporate the action into
        # the field of the new state. Finally, compute the utility of the new state using updateUtility().
        print("getResult")
        state = TicTacToeState()
        # print(self.field)
        state.field = self.field[:]
        # print(state.field)
        state.player = self.player

        if self.playerToMove == Square.X:
            state.playerToMove = Square.O
        else:
            state.playerToMove = Square.X

        state.field[action.position] = action.player
        state.updateUtility()
        return state

    def filledBoxes(self):
        count = 0
        for box in self.field:
            if box == Square.X or Square.O:
                count += 1

        return count

    def  isTerminal(self):
        #TODO Hint: the utility value has specific values if one of
        # the players has won, which is a terminal state. However,
        # you will also have to check for terminal states in which
        # no player has won, which can not be inferred immediately
        # from the utility value.

        # check if all boxes are filled
        if self.filledBoxes == len(self.field):
            return True
        # check if someone won by same row/col/diag
        if self.utility == 1 or self.utility == -1:
            return True

        # otherwise the game is in progress
        return False

    def printresult(self):
        s = "" + self.field[0] + "|" + self.field[1] + "|" + self.field[2] + "\n"
        s += "-+-+-\n"
        s += self.field[3] + "|" + self.field[4] + "|" + self.field[5] + "\n"
        s += "-+-+-\n"
        s += self.field[6] + "|" + self.field[7] + "|" + self.field[8] + "\n"
        print(s)
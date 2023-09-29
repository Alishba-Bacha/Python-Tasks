#Simple Tic Tac Toe Game using if else statements in python
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True

#printing board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def playerInput(board):
    while True:
        if currentPlayer == "X":
            inp = int(input(f"Enter a number 1-9: \tPlayer (X):\t"))
        else:
            inp = int(input(f"Enter a number 1-9:\t Player (0):\t "))
        if inp >= 1 and inp <= 9 and board[inp-1] == "-":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print(f"Oops! Try again! Player Player (X)! ")
            else:
                print(f"Oops! Try again! Player  Player (0)! ")
            printBoard(board)

#check for win or tie
def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
def checkvertical(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Its a tie")
        gameRunning = False
        winner = "None"

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkvertical(board):
        print(f"The winner is {winner}")

#switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#check for win or tie again
while gameRunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()



#GUI code for above programe is
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tic Tac Toe')
        self.setGeometry(100, 100, 300, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        layout = QVBoxLayout()
        self.buttons = []

        self.current_player = 'X'

        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton('', self)
                button.clicked.connect(lambda _, button=button, row=i, col=j: self.button_clicked(button, row, col))
                row.append(button)
                layout.addWidget(button)
            self.buttons.append(row)

        self.central_widget.setLayout(layout)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage(f"Player {self.current_player}'s turn")

    def button_clicked(self, button, row, col):
        if button.text() == '':
            button.setText(self.current_player)
            button.setEnabled(False)
            if self.check_winner(row, col):
                self.show_message(f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_full():
                self.show_message("It's a tie!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_bar.showMessage(f"Player {self.current_player}'s turn")

    def check_winner(self, row, col):
        symbol = self.current_player
        # Check rows
        if all(self.buttons[row][c].text() == symbol for c in range(3)):
            return True
        # Check columns
        if all(self.buttons[r][col].text() == symbol for r in range(3)):
            return True
        # Check diagonals
        if all(self.buttons[i][i].text() == symbol for i in range(3)) or \
           all(self.buttons[i][2 - i].text() == symbol for i in range(3)):
            return True
        return False

    def is_full(self):
        return all(self.buttons[row][col].text() != '' for row in range(3) for col in range(3))

    def show_message(self, message):
        msg = QMessageBox()
        msg.setWindowTitle('Game Over')
        msg.setText(message)
        msg.exec_()

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button.setText('')
                button.setEnabled(True)
        self.current_player = 'X'
        self.status_bar.showMessage(f"Player {self.current_player}'s turn")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())

from player import *


class TicTacToe:
    free_blocks = 9

    def __init__(self):
        self.board = [[' ' for i in range(3)] for i in range(3)]

    def display(self):
        for row in self.board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == ' ':
                    moves.append((row, col))
        return moves

    @staticmethod
    def print_board():
        for row in range(3):
            print("|", end="")
            for col in range(3):
                print(" " + str(row) + "," + str(col) + " |", end="")
            print()

    def check_win(self, letter):
        # rows
        for row in self.board:
            for elem in row:
                if elem != letter:
                    break
            else:
                return True

        # columns
        for col in range(3):
            for row in range(3):
                if self.board[row][col] != letter:
                    break
            else:
                return True

        # diagonals
        for i in range(3):
            if self.board[i][i] != letter:
                break
        else:
            return True

        for i in range(3):
            if self.board[i][2-i] != letter:
                break
        else:
            return True

        return False

    def make_move(self, move, player):
        self.board[move[0]][move[1]] = player.letter


def turn(player, name, game):
    print(f"\n{name}'s turn({player.letter}):-")
    move = player.get_move(game)
    game.make_move(move, player)
    game.free_blocks -= 1
    print(f"\nMove: {move[0]},{move[1]}")
    return game.check_win(player.letter)


def play(player1, player2):
    game = TicTacToe()
    finish = False
    state = True

    # toss to decide who starts
    if random.choice((True, False)):
        state = False

    while not finish:
        if state:
            # player 1's turn
            if turn(player1, "Player 1", game):
                print()
                game.display()
                print("\nPlayer 1 wins!!\n")
                finish = True
        else:
            # player 2's turn
            if turn(player2, "Player 2", game):
                print()
                game.display()
                print("\nPlayer 2 wins!!\n")
                finish = True

        if not game.free_blocks and not finish:
            # all blocks filled and the no one has won, so it is a draw
            print()
            game.display()
            print("\nDraw!\n")
            finish = True

        state = not state

import random


class Player:
    def __init__(self, letter):
        self.letter = letter


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        print("Board:-")
        game.display()
        return random.choice(game.available_moves())


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        row = -1
        col = -1
        while row == -1 and col == -1:
            print("Board:-")
            game.display()
            choice = input("\nPick your move [0-2,0-2]: ")
            if choice == "" or choice.lower() == "help":
                print("\nIndices:-")
                TicTacToe.print_board()
                print()
            else:
                choice = choice.split(",")
                try:
                    if len(choice) < 2:
                        raise ValueError
                    row = int(choice[0])
                    col = int(choice[1])
                    if row > 2 or row < 0 or col > 2 or col < 0:
                        raise Exception(
                            "Index out of range, should be between 0 and 2!\n")
                    if game.board[row][col] != ' ':
                        raise Exception("That block is occupied!\n")
                except ValueError:
                    print("Enter a valid choice!\n")
                except Exception as e:
                    print(e)
                    row = -1
                    col = -1
        return (row, col)

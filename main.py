from game import play
from player import ComputerPlayer, HumanPlayer

def main():
    print("\nWelcome to tic-tac-toe!!\n")
    player1_choice = input("Choose player 1 [human/COMPUTER]: ").lower()
    player1_letter = input("Choose player 1's letter [X/o]: ").upper()
    if player1_letter != 'O':
        player1_letter = 'X'

    if player1_choice == "human":
        player1 = HumanPlayer(player1_letter)
        print(f"Player 1 is a human with {player1.letter}")
    else:
        player1 = ComputerPlayer(player1_letter)
        print(f"Player 1 is the computer with {player1.letter}")

    player2_choice = input("Choose player 2 [human/COMPUTER]: ").lower()
    if player1_letter == 'X':
        player2_letter = 'O'
    else:
        player2_letter = 'X' 
        
    if player2_choice == "human":
        player2 = HumanPlayer(player2_letter)
        print(f"Player 2 is a human with {player2.letter}")
    else:
        player2 = ComputerPlayer(player2_letter)
        print(f"Player 2 is the computer with {player2.letter}")

    print("\nLet's see who wins!")
    play(player1, player2)

if __name__ == "__main__":
    main()



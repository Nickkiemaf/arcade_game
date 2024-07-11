#ARCADE GAME
#Welcomes a player, send a prompt that ask game choice
#1 for RPS : 2 for Guess My Name : "x" to exit
#process the input 
#When player quits a game, they return back to arcade prompt

from enum import Enum
import rps
import guess_number
import _random
import sys

def arcade(name="Playerone"):
		welcome_back =  False

		while True:
			if welcome_back == True:
				print(f"Welcome to the Arcade!\nPlease choose a game:\n")
				arcade_game_choice = input("1 = Rock Paper Scissors\n2 = Guess My Name\n\nOr press 'x' to exit the Arcade\n")
				arcade_game_choice = int(arcade_game_choice)

			if arcade_game_choice not in ([1, 2, "x"]):
				print("Enter 1, 2, or x.\n")
				return arcade(name)
			
			welcome_back = True

			if arcade_game_choice == 1:
				rock_paper_scissors = rps(name)
				rock_paper_scissors() 

			elif arcade_game_choice == 2:
				guess_my_number = guess_number(name)
				guess_my_number()
			
			elif arcade_game_choice == "x":
				sys.exit("Thank you for playing ARCADE!\nHope ypu play again.")
			else:
				print("Wrong input")
				continue


			
#play = arcade()
#play()

if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(
		description="A game where players have access to two different games"
	)

	parser.add_argument(
		"-n", "--name", metavar="name",
		required=True, help="Enter your name", 
	)

	args = parser.parse_args()
	game = arcade(args.name)
	#game()
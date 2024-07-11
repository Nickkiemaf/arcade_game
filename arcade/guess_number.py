#design a guessing game
"""
sends a prompt for player to choose number
receives an input
compares to computer's choice
output winner
output game count
calculates winning percentage
play again prompts and logic: 
"""

import random
import sys
import argparse

def guess_game(name='PlayerOne'):
	game_count = 0
	player_count = 0
	computer_count = 0

	def guess():
		nonlocal name
		nonlocal game_count
		nonlocal player_count
		nonlocal computer_count


		players_choice = input(f"Hi, {name}\nGuess which number I'm thinking of...... 1, 2, or 3.\n")
		#players_choice = int(players_choice)

		computers_choice = random.choice("123")

		if players_choice not in ["1", "2", "3"]:
			print(f"Guess between 1, 2, or 3.")
			return guess()
		
		nonlocal game_count
		game_count+= 1

		def decide_winner():
			if players_choice == computers_choice:
				nonlocal player_count
				player_count += 1
				print(f"\nI was thinking about {players_choice}.\n{name} won!")
			
			else:
				nonlocal computer_count
				computer_count += 1
				print(f"Oops! sorry, {name}. Python wins.")

		winner = decide_winner()
		print(winner)
		print(f"Game count: {game_count}")
		print(f"{name} count: {player_count}")
		print(f"Python count: {computer_count}")

		print(f"\nPlay again?")
		while True:
			play_again = input(f"\nY for yes\nQ to quit.\n")

			if play_again.lower() not in ['y', 'q']:
				continue
			else:
				break

		if play_again.lower() == 'y':
			return guess()
		else:
			print(f"Thank you fpr playing, {name}.\n")
			if __name__ == "__main__":
				sys.exit(f"Bye {name}")
			else:
				return
			
	return guess

if __name__ == "__main__":

	parser = argparse.ArgumentParser(
		description="A guessing game"
	)

	parser.add_argument(
		"-n", "--name", metavar="name",
		required=True, help="Enter your name"
	)

	args = parser.parse_args()
	game = guess_game(args.name)
	game()
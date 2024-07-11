import sys
import random
from enum import Enum

def rps(name='Playerone'):
	game_count = 0
	player_wins = 0
	python_wins = 0


	def play_rps():
		nonlocal name
		nonlocal player_wins
		nonlocal python_wins

		
		class RPS(Enum):
			ROCk = 1
			PAPER = 2
			SCISSORS = 3
		
		playerchoice = input(f"\n{name}, please enter...\n1 for Rock \n2 for Paper\n3 for Scissors\n\n")

		if playerchoice not in ["1", "2", "3"]:
			print(f"{name}, please enter 1, 2, 3")
			return play_rps()

		player = int(playerchoice)

		computerchoice = random.choice([1, 2, 3])
		computer = str(computerchoice)

		print(f"\n{name}, you chose  {str(RPS(player)).split('.')[1]}.")
		print(f"Python chose {str(RPS(computerchoice)).split('.')[1]}.\n")

		def decide_winner(player, computerchoice):
			nonlocal player_wins
			nonlocal python_wins
			nonlocal name
			
			if player == 1 and computerchoice == 3:
				player_wins += 1
				return f"{name}, win!"
			elif player == 2 and computerchoice == 1:
				player_wins += 1
				return f"{name}, win!"
			elif player == 3 and computerchoice == 2:
				player_wins += 1
				return f"{name}, win!"
			elif player == computerchoice:
				return "Tie game!"
			else:
				python_wins += 1
				return f"Python wins\nsorry, {name}"
			
		game_result = decide_winner(player, computerchoice)
		print(game_result)

		nonlocal game_count
		game_count += 1

		print(f"\nGame count: {game_count}")
		print(f"\n{name}'s count: {player_wins}")
		print(f"\nPython count: {python_wins}")

		print(f"\nPlay again, {name}?")
		while True:
			playagain = input("\n Play again? \n Y for Yes \n Q for Quit\n\n")
			if playagain.lower() not in ["y", "q"]:
				continue
			else:
				break
		if playagain.lower() == "y":
			return play_rps()
		else:
			print("\nThank you for playing!\nHope to see you again")
			
			if __name__ == "__main__":
				sys.exit(f"Bye {name}")
			else:
				return
	
	return play_rps


if __name__ == "__main__":
	import argparse

	parser = argparse.ArgumentParser(
		description = "Provides a personalized gaming experience"
	)

	parser.add_argument(
		"-n", "--name", metavar="name",
		required=True, help="The name of person playing the game"
	)

	args = parser.parse_args()

	rock_paper_scissors = rps(args.name)
	rock_paper_scissors()
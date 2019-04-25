# Tic-Tac-Toe w/ "AI" Opponent by Adory Vo
# DESCRIPTION: Play Tic-Tac-Toe against a bot.
# INSTRUCTIONS: Click run and type your inputs to the console into the right.

from re import match
from time import sleep
from sys import exit
from random import (randint, shuffle)

spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 1
first = randint(0, 1)
combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
		  [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]


def board():
	print("\n_{}_|_{}_|_{}_".format(spaces[0], spaces[1], spaces[2]))
	print("_{}_|_{}_|_{}_".format(spaces[3], spaces[4], spaces[5]))
	print(" {} | {} | {} ".format(spaces[6], spaces[7], spaces[8]))


def ai_move():
	shuffle(combos)
	new_combos = []
	for combo in combos:
		Xs = 0
		Os = 0		
		none = ""
		for plrnum in combo:
			num = int(plrnum)
			if spaces[num] == "X":
				Xs += 1
			elif spaces[num] == "O":
				Os += 1
			else:
				none += str(num)
		new_combos.append([Xs, Os, none])

	for i in range(1,4):
		for ncombo in new_combos:
			scenes = [-1, -1, -1, -1, -1]

			def check(boole, none_pos):
				if(boole):
					move = int(ncombo[2][none_pos])
					spaces[move] = str(move+1)
					return move
				return -1

			if i == 1:
				scenes[0] = check(ncombo[0] == 2 and len(ncombo[2]) == 1, 0)
			elif i == 2:
				scenes[1] = check(ncombo[1] == 2 and len(ncombo[2]) == 1, 0)
			elif i == 3:
				scenes[2] = check(len(ncombo[2]) == 2, randint(0, 1))
				scenes[3] = check(len(ncombo[2]) == 1, 0)
				scenes[4] = check(len(ncombo[2]) == 3, randint(0,2))
			for scene in scenes:
				if scene > -1:
					return scene


def win(array):
	row = [spaces[array[0]], spaces[array[1]], spaces[array[2]]]
	if row[0] == row[1] and row[1] == row[2]:
		board()
		if row[0] == "X":
			print("\nComputer wins!")
		else:
			print("\nYou win!")
		exit()


def game():
	global turn
	while True:
		list(map(win, combos))

		if list(filter(lambda x: x not in "123456789", spaces)) == spaces:
			board()
			print("\nIt's a tie!")
			break

		print("{}Turn {}{}".format("-" * 20, turn, "-" * 20))

		if turn % 2 == first:
			board()
			print("It's your turn!")
			pos = input("\nChoose your position! (Input a number 1-9) ")
			if not match(r"^[1-9]{1}$", pos):
				print("\nYou must choose a valid square.")
			elif spaces[int(pos) - 1] not in "123456789":
				print("\nThis square is taken already.")
			else:
				spaces[int(pos) - 1] = "O"
				turn += 1
		else:
			spot = ai_move()
			board()
			print("It's Computer's turn!")
			print("Computer chose " + str(spot+1) + "!")
			spaces[spot] = "X" 
			turn += 1
			sleep(2)


def main():
	print("\nTic-Tac-Toe vs. Bot!\nComputer is X, you are O.")
	game()

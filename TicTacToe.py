spaces = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Tic-Tac-Toe! Player 1 is X, Player 2 is O. Player 1 goes first.")

def combo(s1, s2, s3):
	return "{}, {}, {}".format(spaces[s1], spaces[s2], spaces[s3]).split(", ")

class Break(Exception): pass
def win(row):
	if list(filter(lambda x: x == "X", row)) == row:
		board()
		print("\nPlayer 1 wins!")
		raise Break
	elif list(filter(lambda x: x == "O", row)) == row:
		board()
		print("\nPlayer 2 wins!")
		raise Break

def board():
	print("\n_{}_|_{}_|_{}_".format(spaces[0], spaces[1], spaces[2]))
	print("_{}_|_{}_|_{}_".format(spaces[3], spaces[4], spaces[5]))
	print(" {} | {} | {} ".format(spaces[6], spaces[7], spaces[8]))
	

def game():
	try:
		turn = 1
		while True:
			if list(filter(lambda x: x not in "123456789", spaces)) == spaces:
				board()
				print("\nIt's a tie!")
				break
			
			win(combo(0, 1, 2))
			win(combo(0, 3, 6))
			win(combo(0, 4, 8))
			win(combo(1, 4, 7))
			win(combo(2, 5, 8))
			win(combo(3, 4, 5))
			win(combo(6, 7, 8))
			win(combo(2, 4, 6))
			
			board()
			
			if turn%2 == 0:
				print("It's player 2's turn!")
			else:
				print("It's player 1's turn!")
				
			pos = int(input("\nChoose your position! (Input a number 1-9) "))
			if str(pos) not in "123456789":
				print("\nYou must choose a valid square.")
			elif spaces[pos-1] == "X" or spaces[pos-1] == "O":
				print("\nThis square is taken already.")
			elif turn%2 == 0:
				spaces[pos-1] = "O"
				turn += 1
			else:
				spaces[pos-1] = "X"
				turn += 1
			print("-"*45)
	except Break:
		pass
	except ValueError:
		print("\nInvalid character!")
		turn += 1
		game()
	
game()
	
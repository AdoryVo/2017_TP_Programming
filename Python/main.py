def start():
	response = input("Tic-Tac-Toe!\nType 1 to play against a bot or 2 to play 2-player!\n")
	if(response == "1"):
		import ai
		ai.main()
	elif(response == "2"):
		import multiplayer
    multiplayer.main()
	else:
		print("Invalid response, please type 1 or 2.\n")
		start()

start()

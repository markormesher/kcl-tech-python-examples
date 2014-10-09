print("\nHow to Play:\n\nr = Rock\np = Paper\ns = Scissors\nq = Quit\n\n----\n")

done = False
while (done != True):
	their_move = raw_input("What is your move? [r|p|s|q] ")
	if (their_move == "r"):
		print "You choose rock, I choose paper"
	elif (their_move == "p"):
		print "You choose paper, I choose scissors"
	elif (their_move == "s"):
		print "You choose scissors, I choose rock"
	elif (their_move == "q"):
		print "Bye-bye!"
		done = True
	else:
		print("You didn't pick anything valid!")
	print("")

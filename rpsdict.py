#rps using dictionary
import random
d={"r":"rock","p":"paper","s":"scissor"}
l=("r","p","s")
while True:
	#take input from user
	us=0
	cs=0
	u=input("enter your choice or press n to discontinue")
	#to exit
	if u=="n":
		print("exiting the game now")
		exit(0)
	#input from computer
	c=random.choice(l)
	print("computer chooses",l(d))

	#compare the user and computer choice
	if u==c:
		print("tie")
		print("score is",us==cs)
	elif u=="r" and c=="p":
		print("comp wins")
		print("score is",cs==cs+1)
	elif u=="p" and c=="s":
		print("comp wins")
		print("score is",cs==cs+1)
	elif u=="s" and c=="r":
		print("comp wins")
		print("score is",cs==cs+1)
	else:
		print("u win")
		print("score is",us==us+1)
import random
l=["r","p","s"]
while True:
	#take input from user
	u=input("enter your choice,press n to discontinue")
	#to exit
	if u=="n":
		print("exit")
		exit(0)
	#input from computer
	c=random.choice(l)
	print("computer chooses",c)

	#compare the user and computer choice
	if u==c:
		print("tie")
	elif u=="r" and c=="p":
		print("comp wins")
	elif u=="p" and c=="s":
		print("comp wins")
	elif u=="s" and c=="r":
		print("comp wins")
	else:
		print("u win")
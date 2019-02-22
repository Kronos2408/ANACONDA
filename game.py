import random
while True:
	d = input("\npress r to roll a dice\n press q to quit")
	if d=="r":
		print("you got:",random.randint(1,6))
	if d=="q":
		print("bye!")
		exit()	

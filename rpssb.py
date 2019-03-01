import random

a = ("r", "p", "s")

opt = input("Press B to begin and E to exit ")
if opt == "B":
    p = 0
    c = 0
    print("Lets start the game")

    while True:

        com = random.choice(a)

        player = input("Type r or p or s: ")

        if player == "r" or player == "p" or player == "s":
            print("Computer chose", com, "and You chose", player)

            if (player == "r" and com == "s") or (player == "p" and com == "r") or \
                    (player == "scissors" and com == "papers"):
                print("you win!")
                p = p+1
            elif (player == "s" and com == "r") or\
                    (player == "r" and com == "p") or (player == "p" and com == "s"):
                print("computer wins!")
                c = c+1
            elif player==com:
                print("it's a tie")
            print("Your score is", p, "and Computer's score is", c)
        elif player=="q":
            print("Thanks for playing!")
            quit()
        else:
            print("give a valid input")
        continue

elif opt == "E":
    print("Thanks for not playing!")
quit()




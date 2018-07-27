from random import randint

def rock_user(user, computer):
    if computer == "Paper":
            print("You lose!", computer, "covers", user)
    else:
            print("You win!", user, "smashes", computer)
            
def paper_user(user, computer):
    if computer == "Scissors":
            print("You lose!", computer, "cut", user)
    else:
            print("You win!", user, "covers", computer)
    
def scissor_user(user, computer):
    if computer == "Rock":
            print("You lose...", computer, "smashes", user)
    else:
            print("You win!", user, "cut", computer)

plays = ["Rock", "Paper", "Scissors"]

computer = plays[randint(0,2)]
 
user = False
 
while user == False:
    user = input("Rock, Paper, Scissors?")
    if user.lower() == computer.lower():
        print("Tie!")
    elif user == "Rock":
        rock_user(user, computer)
    elif user == "rock":
        rock_user(user, computer)
    elif user == "Paper":
        paper_user(user, computer)
    elif user == "paper":
        paper_user(user, computer)
    elif user == "Scissors":
        scissor_user(user, computer)
    elif user == "scissors":
        scissor_user(user, computer)
    else:
        print("That's not a valid play. Check your spelling!")

    user = False
    computer = plays[randint(0,2)]


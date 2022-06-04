import random

choices = ["rock", "paper", "scissor"]

computer = random.choice(choices)
player = None
while player not in choices:
    player = input("rock, paper, or scissor?: ")

if player == computer:
    print("computer:", computer)
    print("player:", player)
    print("Tie!")
elif player == "rock":
    if computer == "paper":
        print("computer:", computer)
        print("player:", player)
        print("You Lose!")
    if computer == "scissor":
        print("computer:", computer)
        print("player:", player)
        print("You win!")
elif player == "paper":
    if computer == "rock":
        print("computer:", computer)
        print("player:", player)
        print("You win!")
    if computer == "scissor":
        print("computer:", computer)
        print("player:", player)
        print("You lose!")
elif player == "scissor":
    if computer == "rock":
        print("computer:", computer)
        print("player:", player)
        print("You Lose!")
    if computer == "paper":
        print("computer:", computer)
        print("player:", player)
        print("You Win!")













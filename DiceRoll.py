from random import randint




dice1 = randint(1, 6)
dice2 = randint(1, 3)
total = 0
rounds = 3
rules = ["There are 2 dice.", "the first is numbered 1-6 and the second 1-3", "Each dice gets tossed once for each round"
         , "Your result for the round is equal to the first dice rolls result times the second ones", "There are 3 rounds"
         , "if the result is greater than 20, you win!!"]

print("Welcome to Dice Roll Casino: Here are our rules:")
for rule in rules:
    print("> " + rule)

choice = input("would you like to play our game: type Yes or No: ")
start = False
while True:
    if choice.upper() == "YES":
        start = True
        break
    elif choice.upper() == "NO":
        start = False
        break
    else:
        choice = input("That is not a valid choice: ")
if start:
    curRound = 1
    while curRound <= rounds:
        input("Alright press enter to roll dice for this round: ")
        dice1 = randint(1, 6)
        dice2 = randint(1, 3)
        total += (dice1 * dice2)
        print("Your result for this round is: " + str(dice1*dice2) + '\n')
        curRound+=1
    if total > 20:
        print("you Win, your result was: " + str(total))
    else:
        print("You lost, your result was: " + str(total))


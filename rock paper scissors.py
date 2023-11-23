import random
user = 0
comp = 0
choices = ["rock", "paper", "scissors"]


def after():
    y = input("If you would like to check the score, press E. If you would like to quit, press Q")
    if y.lower() == "e":
        print("User has won " + str(user) + " times")
        print("Computer has won " + str(comp) + " times")
    if y.lower() == "q":
        quit()


while True:
    user_throw = input("If you want to play, type Rock, Paper, or Scissors. If you want to quit or check score type Q ").lower()
    if user_throw == "q":
        break
    if user_throw not in choices:
        print("Please type rock, paper or scissors")
        continue
    x = random.randint(0, 2)
    comp_throw = choices[x]
    print("Computer threw " + str(comp_throw))

    if user_throw == "rock" and comp_throw == "scissors":
        print("You won!")
        user += 1
    if user_throw == "paper" and comp_throw == "rock":
        print("You won!")
        user += 1
    if user_throw == "scissors" and comp_throw == "paper":
        print("You won!")
        user += 1
    if user_throw == "rock" and comp_throw == "paper":
        print("You lost!")
        comp += 1
    if user_throw == "scissors" and comp_throw == "rock":
        print("You lost!")
        comp += 1
    if user_throw == "paper" and comp_throw == "scissors":
        print("You lost!")
        comp += 1
    if user_throw == "scissors" and comp_throw == "scissors":
        print("It's a tie!")
    if user_throw == "paper" and comp_throw == "paper":
        print("It's a tie!")
    if user_throw == "rock" and comp_throw == "rock":
        print("It's a tie!")
    again = input("Want to play again? ")
    if again.lower() == "yes":
        continue
    else:
        after()

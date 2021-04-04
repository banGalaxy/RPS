import random
#declaring the different variables
outcome_list = ["rock", "paper", "scissors"]
win = [("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")]
counter = 0



def check_pick():
    user_pick = input("What would you like to choose? > ").lower()
    compare = (user_pick, comp_pick)
    print(compare)
    global counter
    if user_pick != comp_pick:
        if user_pick in outcome_list:
            if compare in win:                
                counter += 1
                print("You won")
            else:
                print("Sorry, you lost, try again.")
        else:
            print("Sorry, that is not an option, try again.")
    else:
        print("It looks like you drew.")
    print("Score is ", counter)
while True:
    comp_pick = outcome_list[(random.randint(0, 2))]
    check_pick()

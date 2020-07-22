import random
import time

def intro():
 print("hello whats your name ?")
 name = input("-")
 print("well..."+name.title()+" we are going to play rock, paper, scissors!")
 print()
intro()


def results():
    action = random.choice(("Rock", "Paper", "Scissors"))

    print("what are you going to play ?(rock, paper, scissors)")
    playersAction = input("-")

    if playersAction.title() == action :
     print("Hmmm, my turn!...I play...")
     time.sleep(1)
     print()
     print(action.title())
     print()
     print('Tie!')
    elif playersAction.title() == "Rock" and action == "Paper":
     print("Hmmm, my turn!...I play...")
     time.sleep(1)
     print()
     print(action.title())
     print()
     print("paper covers rock, You lose!")
    elif playersAction.title() == "Rock" and action == "Scissors":
     print("Hmmm, my turn!...I play...")
     time.sleep(1)
     print()
     print(action.title())
     print()
     print("Rock destroys scissors, You win!")
    elif playersAction.title() == "Paper" and action =="Scissors":
        print("Hmmm, my turn!...I play...")
        time.sleep(1)
        print()
        print(action.title())
        print()
        print("Scissors cuts paper, You lose!")
    elif playersAction.title() == "Paper" and action == "Rock":
        print("Hmmm, my turn!...I play...")
        time.sleep(1)
        print()
        print(action.title())
        print()
        print("Paper covers rock, You win!")
    elif playersAction.title() == "Scissors" and action == "Rock":
        print("Hmmm, my turn!...I play...")
        time.sleep(1)
        print()
        print(action.title())
        print()
        print("Rock destroys scissors, You lose!")
    elif playersAction.title() == "Scissors" and action == "Paper":
        print("Hmmm, my turn!...I play...")
        time.sleep(1)
        print()
        print(action.title())
        print()
        print("Scissors cuts paper, You win!")
    else:
        print("You probably misspelled a word!")

results()
print("\tPlay again ?(yes/no)")
playagain = input("-")
while playagain == "yes" or playagain == "y":
    results()
    print("\tPlay again ?(yes/no)")
    playagain = input("-")

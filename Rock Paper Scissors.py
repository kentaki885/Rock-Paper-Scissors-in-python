import time
import random


def intro():
    '''Greeting user'''

    name = input('\nHello! Whats your name ? ').title()
    print(f'Well ... {name} we are going to play scissors, paper, rock\n')


def output(action, message):
    '''Deliver message with action each time when user wins / lose the game'''

    print('\nHmmm, My Turn! .... I Play ... \n')
    time.sleep(1)
    print(action.title() + '\n')
    print(message + '\n')


def playing():
    '''Asking user to enter their choice and deciding who won the game'''

    action = random.choice(("Rock", "Paper", "Scissors"))
    player_action = input('what are you going to play ?(Scissors, Paper, Rock): ').title()

    if player_action == action:
        output(action, 'Tie!')

    elif player_action == "Rock" and action == "Paper":
        output(action, 'Paper covers Rock, You lose!')

    elif player_action == "Rock" and action == "Scissors":
        output(action, 'Rock destroys scissors, You win!')

    elif player_action == "Paper" and action == "Scissors":
        output(action, 'Scissors cuts Paper, You lose!')

    elif player_action == "Paper" and action == "Rock":
        output(action, 'Paper covers Rock, You win!')

    elif player_action == "Scissors" and action == "Rock":
        output(action, 'Rock destroys scissors, You lose!')

    elif player_action == "Scissors" and action == "Paper":
        output(action, 'Scissors cuts Paper, You win!')

    else:
        print("You probably misspelled a word!")


def main():
    '''Entry of the program'''

    while True:
        intro()
        playing()

        option = input('Do you want to play again (y/n)? ').lower()

        if option != 'y':
            break   # Breaking while loop

        print()


if __name__ == '__main__':
    main()

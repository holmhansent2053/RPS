import random

# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def string_checker(question, valid_ans=('yes', 'no')):

    error = f"Please enter an option from {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item


            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item


        # print error if user does not enter something that is valid
        print(error)
        print()


def instructions():
    print('''
**** Instructions *****
To begin, choose the number of rounds(or choose infinite mode).
Then play against the computer. You need to choose paper, scissors, or rock.

The rules are as follows:
Paper beats rock
Rock beats scissors
Scissors beats paper

Press <xxx> to end the game at any time

Good luck
    ''')

# Main Routine Starts here

# Initialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]

print("💎📰✂ Rock / Paper / Scissors Game 💎📰✂")
print()

# ask user if they want to see the instructions and display
# them if requested
want_instructions = string_checker("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:


    user_choice = input("Choose: ")
   
    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

    # Game loop ends here

    # Game History / Statistics area



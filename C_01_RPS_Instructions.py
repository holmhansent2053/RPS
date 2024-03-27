# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).Lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


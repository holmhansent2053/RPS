def rps_compare(user, comp):

    if comp == user:
        var_result = "tie"

    # Three ways to win...
    elif comp == "rock" and user == "paper":
        var_result = "win"

    # if it's not a win / tie, it's a loss
    else:
        var_result = "loss"

    return var_result

#  testing loop
while True:
    user_choice = input("user choice: ")
    comp_choice = input("computer choice: ")

    result = rps_compare(user_choice, comp_choice)
    print(result)
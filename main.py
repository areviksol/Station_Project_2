import random

def dice_number():
    _ = input("Press Enter to roll the dice: ")

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2

def display_dices(dices):
    die1, die2 = dices
    print("The sum of numbers you have got in die 1 and die 2 are {} + {} = {}".format(die1, die2, sum(dices)))

value = dice_number()
display_dices(value)
sum_of_dices = sum(value)

if sum_of_dices in (7, 11):
    result = "Congratulations, you won!"
elif sum_of_dices in (2, 3, 12):
    result = "Sorry, you lost. Try again next time."
elif sum_of_dices in (4, 5, 6, 8, 9, 10):
    result = "Continue your game, please."
    current_point = sum_of_dices
    print("Your current point is", current_point)

while result == "Continue your game, please.":
    value = dice_number()
    display_dices(value)
    sum_of_dices = sum(value)

    if sum_of_dices == current_point:
        result = "Congratulations, you won!"
    elif sum_of_dices == 7:
        result = "Sorry, you lost. Try again next time."

print(result)

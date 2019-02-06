import random
from collections import defaultdict

def main_roll():
    dice_amount = int(input("Enter the number of dice: "))                  # Total Number of Dice Being Rolled
    sides_of_dice = int(input("Enter the number of sides: "))               # Total Number of Sides per Die
    rolls_of_dice = int(input("Enter the number of rolls to simulate: "))   # Total Number of Times Each Die Rolled
    result = roll(dice_amount, sides_of_dice, rolls_of_dice)                # This stores the results
    maxH = 0                                                                # Used for formulating

    for i in range(dice_amount, dice_amount * sides_of_dice + 1):
        if result[i] / rolls_of_dice > maxH: maxH = result[i] / rolls_of_dice
    for i in range(dice_amount, dice_amount * sides_of_dice + 1):
        print('{:2d}{:10d}{:8.2%} {}'.format(i, result[i], result[i] / rolls_of_dice, '#' * int(result[i] / rolls_of_dice / maxH * 40)))


def roll(dice_amount, sides_of_dice, rolls):
    d = defaultdict(int)
    for _ in range(rolls):
        d[sum(random.randint(1, sides_of_dice) for _ in range(dice_amount))] += 1
    return d

main_roll()
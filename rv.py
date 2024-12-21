#!/Users/ishitajain/anaconda3/bin/python
import math
import random

def pmf():
    p = 0
    for x in range(2, 12+1):
        pr_x = two_dice_roll_sum(x)
        p += x*pr_x
    print(p)

def two_dice_roll_sum(x):
    count = 0
    for dice_1 in range(1, 7):
        for dice_2 in range(1, 7):
            if dice_1 + dice_2 == x:
                count += 1
    return count / 36


pmf()


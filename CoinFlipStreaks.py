# Calculates chance of 6 heads or tails values in a row (sample size = 50000)

import random

numberOfStreaks = 0
SAMPLESIZE = 50000


for experimentNumber in range(SAMPLESIZE):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listOfFlips = []
    while True:
        if len(listOfFlips) == 100:
            break

        # 0 = Heads, 1 = Tails
        listOfFlips.append(random.randint(0,1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for index, item in enumerate(listOfFlips):
        if index >= 5:
            if (item == listOfFlips[index - 1]) and (item == listOfFlips[index - 2]) and (item == listOfFlips[index - 3]) and (item == listOfFlips[index - 4]) and (item == listOfFlips[index - 5]):
                numberOfStreaks += 1

numberOfStreaks /= SAMPLESIZE
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
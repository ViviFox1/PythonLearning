#This is a Rock, Paper, Scissors game.
import random, sys

numWins = 0
numLosses = 0
numDraws = 0


while True: #main loop'

    print(str(numWins) + ' WINS, ' + str(numLosses) + ' LOSSES, ' + str(numDraws) + ' DRAWS')

    while True: #input loop
        print('Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit')
        guess = input()
        if guess == 'q':
            sys.exit()
        if guess == 'r' or guess == 'p' or guess == 's':
            break
        print('Enter "r", "p", "s", or "q".')

    #display player choice
    if guess == 'r':
        print('ROCK versus...')
    if guess == 'p':
        print('PAPER versus...')
    if guess == 's':
        print('SCISSORS versus...')

    #determine cpu choice
    randomNumber = random.randint(0,2)
    if randomNumber == 0:
        cpuGuess = 'r'
        print('ROCK')
    if randomNumber == 1:
        cpuGuess = 'p'
        print('PAPER')
    if randomNumber == 2:
        cpuGuess = 's'
        print('SCISSORS')
    print("")

    #determine winner
    if guess == cpuGuess:
        print('DRAW')
        numDraws += 1
    if guess == 'p' and cpuGuess == 's':
        print('YOU LOSE')
        numLosses += 1
    if guess == 's' and cpuGuess == 'r':
        print('YOU LOSE')
        numLosses += 1
    if guess == 'r' and cpuGuess == 'p':
        print('YOU LOSE')
        numLosses += 1
    if guess == 's' and cpuGuess == 'p':
        print('YOU WIN')
        numWins += 1
    if guess == 'p' and cpuGuess == 'r':
        print('YOU WIN')
        numWins += 1
    if guess == 'r' and cpuGuess == 's':
        print('YOU WIN')
        numWins += 1

#This is a guess the number game.
import random

correctGuess = False
numGuess = 0
correctAnswer = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')
while correctGuess != True:
    print('Make a guess!')
    guess = int(input())
    if guess < 1 or guess > 20:
        print('Not in range!')
        numGuess += 1
        continue
    elif guess < correctAnswer:
        print('Too low!')
        numGuess += 1
        continue
    elif guess > correctAnswer:
        print('Too high!')
        numGuess += 1
        continue
    elif guess == correctAnswer:
        print('Correct!')
        numGuess += 1
        break
    else:
        print('Error')
if numGuess == 1:
    print('It took you ' + str(numGuess) + ' attempt to guess correctly.')
else:
    print('It took you ' + str(numGuess) + ' attempts to guess correctly.')



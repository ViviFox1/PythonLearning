#Black magic wtf
#Repeats a function until the resulting number is 1
collatzCount = 0
def collatz(number):
    if(number % 2 == 0): #if number is even
        result = number // 2
        print(result)
        return result
    else: #if number is odd
        result = 3 * number + 1
        print(result)
        return result

print('Enter a non-zero integer:')
inputNumber = int(input())
print('Starting with ' + str(inputNumber) + '...')

currentNumber = inputNumber
while currentNumber != 1:
    currentNumber = collatz(currentNumber)
    collatzCount += 1

print('You went from', str(inputNumber), 'to', str(currentNumber), 'in', str(collatzCount), 'steps!')
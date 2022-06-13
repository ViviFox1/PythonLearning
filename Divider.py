#divide 2 numbers with divide by 0 exception handling

def numberDivider(num1, num2):
    try:
        return num1 / num2
    except: 
        print('Error: Invalid argument.')



while True:
    print('Input first number (dividend):')
    try:
        input1 = input()
        input1 = int(input1)
        break
    except:
        print('Error: Invalid argument.')

while True:
    print('Input second number (divisor):')
    try:
        input2 = input()
        input2 = int(input2)
        break
    except:
        print('Error: Invalid argument.')

print('Dividing', str(input1), 'by', str(input2), '...')
result = numberDivider(input1, input2)
print('The result is', str(result))
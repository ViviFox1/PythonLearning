#This is a program that says "Hello" then asks for the user's name

print('Hello!')
print('What is your name?')
userName = input()
print('Nice to meet you ' + userName + '!')
print('The length of your name is ' + str(len(userName)) + ' characters long.')

print('How old are you?')
userAge = input()
print('You will be ' + str(int(userAge)+1) + ' years old next year.')

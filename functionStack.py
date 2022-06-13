#Demo of how function stacks work

def functionA():
    print('A starts')
    functionB()
    functionD()
    print('A returns')

def functionB():
    print('B starts')
    functionC()
    print('B returns')

def functionC():
    print('C starts')
    print('C returns')

def functionD():
    print('D starts')
    print('D returns')

functionA()
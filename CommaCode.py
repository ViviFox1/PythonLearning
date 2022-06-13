
#input: list ('apple', 'banana', 'orange')
#output: string ('apple, banana, and orange')


def ListPrinter(startingList):
    if len(startingList) == 0:
        print('')

    elif len(startingList) == 1:
        print(startingList[0])

    else:
        for index, item in enumerate(startingList):
            if index == len(startingList) - 1 :
                print('and', item)
            
            else:
                print(str(item) + ', ', end='')

ListPrinter(['apple', 'banana', 'orange'])
ListPrinter([93])
ListPrinter([])
ListPrinter([72.3, 88.9])        


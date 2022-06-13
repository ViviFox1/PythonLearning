def GridPrinter(listOfLists):
    # Takes a list of lists and prints out a grid based on input
    # Transposes grid
    # assuming x,y:
    # print 0,0 ; 1,0 ; 2,0 ; etc
    # print 0,1 ; 1,1 ; 2,1 ; etc
    # etc
    x = 0
    y = 0

    while y < len(listOfLists[0]): # iterate through y's, assume each list within list of lists is same size (grid)
        x = 0
        while x < len(listOfLists): # iterate through x's for a given y

            # line break only if last entry for given y
            if x < len(listOfLists)-1:
                print(listOfLists[x][y], end='')
            else:
                print(listOfLists[x][y])

            x += 1
        y += 1

GridPrinter([['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']])
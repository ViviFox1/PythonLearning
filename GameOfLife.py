""""
Simulates Conway's Game of Life
List should look like:
[
    [#, , ,#,#]
    [#,#,#, , ]
    etc
]
"""
import random, time, copy


WIDTH = 60
HEIGHT = 20

increment = 0

# Create a list of lists for the cells:
nextCells = []

# Create a starting grid
for x in range(WIDTH):
    column = [] # Make a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#') # Live cell
        else:
            column.append(' ') # Dead cell
    nextCells.append(column)
    
while increment < 25: # Main loop
    print('\n\n\n\n\n') # Seperates each step
    currentCells = copy.deepcopy(nextCells)

    #Print current cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') # print the cell
        print() # line break at end of row

    # Calculate the next step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):

            # Get neighbooring coordinates
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            upCoord = (y + 1) % HEIGHT
            downCoord = (y - 1) % HEIGHT

            # Check number of living neighbors
            numNeighbors = 0

            if currentCells[leftCoord][upCoord] == '#':
                numNeighbors += 1
            
            if currentCells[x][upCoord] == '#':
                numNeighbors += 1
            
            if currentCells[rightCoord][upCoord] == '#':
                numNeighbors += 1
            
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1
            
            if currentCells[x][y] == '#':
                numNeighbors += 1
            
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1

            if currentCells[leftCoord][downCoord] == '#':
                numNeighbors += 1
            
            if currentCells[x][downCoord] == '#':
                numNeighbors += 1
            
            if currentCells[rightCoord][downCoord] == '#':
                numNeighbors += 1

            # Set status in next state
            if currentCells[x][y] == '#':
                # if cell is alive
                if numNeighbors == 2 or numNeighbors == 3:
                    nextCells[x][y] = '#'
                else:
                    nextCells[x][y] = ' '
            else:
                #if cell is dead
                if numNeighbors == 3:
                    nextCells[x][y] = '#'
                else:
                    nextCells[x][y] = ' '
    
    # Add small delay
    time.sleep(1)
    increment += 1


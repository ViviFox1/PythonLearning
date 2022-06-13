#outputs a zigzag pattern

import time, sys

indent = 0
totalTime = 0
indentIncreasing = True


while totalTime < 10: #Main loop, runs for 10 seconds
    print(' ' * indent, end='')
    print('******')
    time.sleep(0.1)
    totalTime += 0.1
    if indentIncreasing:
        #increase the indent by 1
        indent += 1
        if indent == 20:
            indentIncreasing = False
    else:
        #decrease the indent by 1
        indent -= 1
        if indent == 0:
            indentIncreasing = True

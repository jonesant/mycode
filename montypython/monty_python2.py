#!/usr/bin/env python3
round = 0  # this is a counter to control the While loop
while(True):  # this is a forever loop, until we execute a break.  Also you need to indent the next line after the While loop
    round = round + 1  #this is a variable counter
    print('Finish the movie title,  "Monty Python\'s The life of ______"')
    answer = input()

    if (answer == 'Brian'):
        print('Correct')
        break
    elif(round==3):
        print('Sorry, the answer was Brian.' )
        break   # Break statement escape the while loop
    else:      # if answer was wrong, and round is not yet equal to 3
        print('Sorry, Try again!')
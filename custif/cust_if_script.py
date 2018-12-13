#!/usr/bin/env python3
message = 'Then your grade will be '
print('What is your numeric score?')
grade = float(input())
if grade >= 90:
    message = message + 'Then your grade will be an A'
elif grade  >= 80 or grade <= 89:
    message = message + 'Then you grade will be a B'
elif grade >= 70:
    message = message + 'Then your grade will be a C'
elif grade >= 60:
    message = message + 'Then your grade will be a D'
elif grade >= 50:
    message = message + 'Then your grade will be a F'
print(message)

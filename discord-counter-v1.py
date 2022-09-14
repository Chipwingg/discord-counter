"""
Created on Sat Sep 10 23:10:50 2022

@author: Chipwingg
"""

import pyautogui
import keyboard
import time
import random

# Ask for the starting number, and assigns it to NUMBER.
NUMBER = int(input('Starting number: '))

# Double checks that you typed the correct number.
print('\n'f'Starting number is {NUMBER}, correct?')
ANSWER = input('Type y or n: ')
time.sleep(0.5)

# If you typed the wrong number, ends script.
if(ANSWER != 'y'):
    print('Oops, try again.')
    exit()

# I learned how to use def, although unnecesary here. 
# This gives a countdown before starting to type. 
def welcome():
    print('\nMove your cursor to text box!')
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)
    print('Running... (Press ESC to exit)')
    time.sleep(1)

welcome()

# Writes out the starting number.
pyautogui.write(str(NUMBER), interval=0.25)

# Until you press ESC key, loop listens for the enter key
# and types NUMBER incremented by 2. 
while keyboard.read_key() !='esc':
    if keyboard.is_pressed('enter'):
        NUMBER = NUMBER + 2
        RANDOMNESS = random.uniform(0.2,0.45)
        time.sleep(1)
        pyautogui.write(str(NUMBER), interval=RANDOMNESS)
        #print(RANDOMNESS)

# If you end the loop, (ESC), script ends after this.        
print('Script ended successfully.')

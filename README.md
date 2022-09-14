# discord-counter
Semi-automated counter script for discord counting games. 

### Why did I make this?

I made this script because I was lazy, and wanted to stop making errors when playing a counting game on a discord server. 

If you don't know what that is, here is a discord bot that makes playing this game very easy. [Here](https://github.com/CircuitSacul/Minigames) is the github repo, and [here](https://discord.gg/dGAzZDaTS9) is the developers discord server.

# Requirements
I wrote/tested this on Ubuntu 21.10, but it should work on most linux platforms. Let me know if you use it on another platform without needing to edit the script. 

+ Python 3.9.7
+ `sudo` permissions 
+ `pyautogui`, `keyboard`, `time`, and `random` libraries installed with `sudo pip install`.

This script __has__ to be run with sudo, otherwise, it will not work. The reason is so the `keyboard` library can see what keys you're pressing down. 

# Usage
+ Download the discord-counter-vx.py file, or copy and paste the code into a .py file you create. 
+ Open a terminal, and `cd` to the where you put the file. 
+ Run `sudo python3 counter-vx.py` (adjust the file name to match what you have on your computer). 
+ Follow the prompts!
